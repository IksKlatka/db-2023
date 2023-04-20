from dataclasses import dataclass

@dataclass
class CastEntry:
    movie_index: int
    cast_id: int
    character: str
    credit_id: str
    gender: int
    id: int
    name: str
    order: int

@dataclass
class CrewEntry:
    movie_index: int
    credit_id: int
    department: str
    gender: int
    id: int
    job: str
    name: str