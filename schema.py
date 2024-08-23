from pydantic import BaseModel


class Book(BaseModel):
    title: str
    rating: int
    author_id: int

    class Config:
        from_attributes = True


class Author(BaseModel):
    name: str
    bio: str
    age: int

    class Config:
        from_attributes = True
