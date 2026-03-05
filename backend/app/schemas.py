from pydantic import BaseModel

class SourceBase(BaseModel):
    name: str
    url: str

class SourceCreate(SourceBase):
    pass

class Source(SourceBase):
    id: int

    class Config:
        orm_mode = True