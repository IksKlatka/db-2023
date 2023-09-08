from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass
class User:
    uid: UUID
    name: str


@dataclass
class Election:
    eid: UUID
    name: str

@dataclass
class Participation:
    uid: UUID
    eid: UUID

@dataclass
class Token:
    eid: UUID
    tokenid: UUID


@dataclass
class Vote:
    eid: UUID
    votevalue: int


class VotingError(RuntimeError):
    pass


if __name__ == '__main__':
    try:
        raise VotingError('ha ha ha')
    except RuntimeError as e:
        print(e)
