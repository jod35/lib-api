from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.models import Book
from .schemas import BookCreateModel
from sqlmodel import select

class BookService:
    def __init__(self,session:AsyncSession):
        self.session = session

    async def get_all_books(self):
        statement = select(Book).order_by(Book.created_at)

        result = await self.session.exec(statement)

        return result.all()
    
    async def create_book(self,book_create_data:BookCreateModel):
        new_book = Book(
            **book_create_data.model_dump()
        )
        
        self.session.add(new_book)

        await self.session.commit()

        return new_book
    
    async def get_book(self,book_uid:str):
        statement = select(Book).where(Book.uid == book_uid)

        result = await self.session.exec(statement)

        return result.first()
    
    async def update_book(self,book_uid:str,book_update_data:BookCreateModel):

        statement = select(Book).where(Book.uid == book_uid)

        result = await self.session.exec(statement)

        book = result.first()

        for key , value in book_update_data.model_dump().items():
            setattr(book, key,value)

        await self.session.commit()

        return book

    async def delete_book(self,book_uid):
        statement = select(Book).where(Book.uid == book_uid)
        result = await self.session.exec(statement)

        book = result.first()

        await self.session.delete(book)

        await self.session.commit()
