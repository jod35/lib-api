from src.db.models import Book
from pydantic import BaseModel

class BookResponseModel(Book):
    pass


class BookCreateModel(BaseModel):
    title:str
    author:str
    isbn:str
    description:str

    model_config ={
        "json_schema_extra":{
            "example":{
                "title": "Python Cookbook",
                "author": "John Doe",
                "isbn": "978-1-4939-1387-3",
                "description": "Python Cookbook is a collection of books written by <NAME> and <NAME>."
            }
        }
    }
