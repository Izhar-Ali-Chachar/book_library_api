from typing import Any
from fastapi import FastAPI

books = [
    {
        "id": 1,
        "name": "To Kill a Mockingbird",
        "genre": "Fiction",
        "author": "Harper Lee",
        "published_date": "1960-07-11"
    },
    {
        "id": 2,
        "name": "1984",
        "genre": "Dystopian",
        "author": "George Orwell",
        "published_date": "1949-06-08"
    },
    {
        "id": 3,
        "name": "The Great Gatsby",
        "genre": "Classic",
        "author": "F. Scott Fitzgerald",
        "published_date": "1925-04-10"
    },
    {
        "id": 4,
        "name": "The Hobbit",
        "genre": "Fantasy",
        "author": "J.R.R. Tolkien",
        "published_date": "1937-09-21"
    },
    {
        "id": 5,
        "name": "Pride and Prejudice",
        "genre": "Romance",
        "author": "Jane Austen",
        "published_date": "1813-01-28"
    }
]

app = FastAPI()

@app.get('books')
def get_books(id: int) -> dict[int, Any]:
    for book in books:
        if book['id'] == id:
            return book