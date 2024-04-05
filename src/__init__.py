from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.db.main import init_db
from src.books.routes import book_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("server is starting")
    await init_db()
    yield
    print("server is shutting down")


app = FastAPI(
    title="Book service",
    version="0.1.0",
    description="A simple web service for a book application",
    lifespan=lifespan,
)


app.include_router(book_router, tags=["books"])
