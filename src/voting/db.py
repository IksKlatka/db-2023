import asyncio
import uuid
from asyncio import run, create_task
from datetime import datetime
from os import getenv
from random import choice

import asyncpg
from dotenv import load_dotenv

from model import *

load_dotenv()
URL = getenv('DATABASE_URL')
SCHEMA = getenv('SCHEMA')




class DbService:

    async def initialize(self):
        self.pool = await asyncpg.create_pool(URL, timeout=30, command_timeout=5,
                                              server_settings={'search_path': SCHEMA})

        print(f'connected to [{URL}]')

    async def create_user(self, user: User) -> User:
        query = """
               INSERT INTO users (uid, name) VALUES ($1, $2) RETURNING *
           """
        values = (user.uid, user.name)
        async with self.pool.acquire() as connection:
            result = await connection.fetchrow(query, *values)
        res = User(*result)
        print(f'Created user: {res}')
        return res

    async def delete_user(self, uid: uuid):
        query = """
               DELETE FROM users WHERE uid = $1
           """
        async with self.pool.acquire() as connection:
            await connection.execute(query, uid)
            print(f'Removed user {uid}')

    async def get_user(self, uid: uuid):
        async with self.pool.acquire() as connection:
            result = await connection.fetchrow("SELECT * FROM users WHERE uid=$1", uid)
            if result:
                return True
            return False

    async def create_election(self, election: Election) -> Election:
        query = """
               INSERT INTO elections (eid, name) VALUES ($1, $2) RETURNING *
           """
        values = (election.eid, election.name)
        async with self.pool.acquire() as connection:
            result = await connection.fetchrow(query, *values)
        res = Election(*result)
        print(f'Created election: {res}')
        return res

    async def delete_election(self, eid: uuid):
        query = """
               DELETE FROM elections WHERE eid = $1
           """
        async with self.pool.acquire() as connection:
            await connection.execute(query, eid)
            print(f'Removed election {eid}')

    async def get_election(self, eid: uuid):
        async with self.pool.acquire() as connection:
            result = await connection.fetchrow("SELECT * FROM elections WHERE eid=$1", eid)
            if result:
                return True
            return False

    async def register_for_election(self, eid: uuid, uid: uuid) -> uuid:
        """
        User with `uid` registers for election `eid`; raises VotingError if already voted, or
        `uid` or `eid` are invalid.

        Transactional.

        :param eid:
        :param uid:
        :return: token for the election
        """
        async with self.pool.acquire() as connection:
            if await self.get_election(eid) == False or await self.get_user(uid) == False:
                return "Either user or election does not exist. (or both!)"

            result = await connection.fetchrow("INSERT INTO participation (user_id, election_id) "
                                               "VALUES ($1, $2) RETURNING *", uid, eid)
            res = Participation(*result)
            print(f"Created participation: {res}.")

            result = await connection.fetchrow("INSERT INTO tokens (eid, tokenid) VALUES ($1, $2) "
                                                "RETURNING *", eid, uuid.uuid4())
            res = Token(*result)
            print(f"Created token for election: {eid}")

            return res.tokenid

    async def get_token_by_tokenid(self, tokenid: uuid):

        async with self.pool.acquire() as connection:
            token = await connection.fetchrow("SELECT * FROM tokens WHERE tokenid=$1", tokenid)
            if token:
                result = Token(*token)
                return result
            return False


    async def vote(self, tokenid: uuid, votevalue: int) -> uuid:
        """
        User with token `tokenid` votes in election. Appropriate row is created in Votes; token is removed.


        Transactional.

        :param eid:
        :param uid:
        :raises: VotingError if tokenid is invalid
        :return:
        """
        async with self.pool.acquire() as connection:
            get_token = await connection.fetchrow("SELECT * FROM tokens WHERE tokenid=$1", tokenid)
            if not get_token:
                raise VotingError("Invalid token!")
            result = Token(*get_token)
            voting = await connection.fetch("INSERT INTO votes (eid, votevalue) VALUES ($1, $2)",
                                            result.eid, votevalue)
            print("Vote accepted.")
            del_token = await connection.fetch("DELETE FROM tokens WHERE tokenid=$1", tokenid)
            print("Token deleted.")


def ts():
    return datetime.now().timestamp()


async def main():
    db = DbService()
    await db.initialize()
    uid = uuid4()
    user = await db.create_user(User(uid, 'xi'))
    # await db.delete_user(user.uid)
    eid = uuid4()

    elect = await db.create_election(Election(eid, 'Wybory normalne'))
    # await db.delete_election(elect.eid)

    register = await db.register_for_election(uid=uid, eid=eid)
    voting = await db.vote(tokenid=register, votevalue=2)



if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    run(main())
