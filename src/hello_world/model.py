from dataclasses import dataclass
from datetime import datetime
from uuid import UUID, uuid4


@dataclass
class User:
    uid: UUID
    username: str
    password: str
    created_at: datetime
    updated_at: datetime


if __name__ == '__main__':
    u1 = User(uuid4(), 'Nabuchodonozor', '666', datetime.now(), datetime.now())
