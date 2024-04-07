from src.db.models import Book
from pydantic import BaseModel


class BookResponseModel(Book):
    """
        This class is used to validate the response when getting book objects
    """
    pass


class BookCreateModel(BaseModel):
    """
        This class is used to validate the request when creating or updating a book
    """
    title: str
    author: str
    isbn: str
    description: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Python Cookbook",
                "author": "John Doe",
                "isbn": "978-1-4939-1387-3",
                "description": "Python Cookbook is a collection of books written by <NAME> and <NAME>.",
            }
        }
    }
