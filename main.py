import os
import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
from dotenv import load_dotenv

from models import Book as ModelBook, Author as ModelAuthor
from schema import Book as SchemaBook, Author as SchemaAuthor

load_dotenv(".env")

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


@app.get('/')
async def root():
    return {'message': 'Hello, world'}


@app.post("/add-book", response_model=SchemaBook)
async def add_book(book: SchemaBook):
    db_book = ModelBook(
        title=book.title, rating=book.rating, author_id=book.author_id)
    db.session.add(db_book)
    db.session.commit()
    return db_book


@app.post("/add-author", response_model=SchemaAuthor)
async def add_author(author: SchemaAuthor):
    db_author = ModelAuthor(name=author.name, bio=author.bio, age=author.age)
    db.session.add(db_author)
    db.session.commit()
    return db_author


@app.get("/books/")
async def get_books():
    books = db.session.query(ModelBook).all()
    return books


if __name__ == "__main__":
    uvicorn.run("app", port=8000, reload=True)
