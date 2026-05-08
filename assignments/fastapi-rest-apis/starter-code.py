from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Book API Starter")


class BookCreate(BaseModel):
    title: str
    author: str
    year: int


class Book(BookCreate):
    id: int


BOOKS = [
    {"id": 1, "title": "Clean Code", "author": "Robert C. Martin", "year": 2008},
    {
        "id": 2,
        "title": "The Pragmatic Programmer",
        "author": "Andrew Hunt and David Thomas",
        "year": 1999,
    },
]


@app.get("/books")
def list_books():
    """Return all books."""
    return BOOKS


@app.get("/books/{book_id}")
def get_book(book_id: int):
    """Return a single book by id."""
    for book in BOOKS:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books", status_code=201)
def create_book(payload: BookCreate):
    """Create a new book and return it."""
    next_id = max((book["id"] for book in BOOKS), default=0) + 1
    new_book = Book(id=next_id, **payload.model_dump())
    BOOKS.append(new_book.model_dump())
    return new_book


# TODO: Task 3
# Add PUT /books/{book_id} to update an existing book.
# Add DELETE /books/{book_id} to remove an existing book.


@app.get("/")
def root():
    return {"message": "Book API starter is running"}
