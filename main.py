import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager

from logger import logger
from auth.router import router as auth_router
from contacts.router import router as contacts_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Додаток успішно запущено.")
    yield
    logger.info("Зупинка додатка...")


app = FastAPI(
    title="Contacts REST API",
    description="Застосунок для управління контактами з модульною структурою та JWT авторизацією.",
    version="2.0.0",
    lifespan=lifespan
)

# Підключення модульних роутерів
app.include_router(auth_router)
app.include_router(contacts_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)