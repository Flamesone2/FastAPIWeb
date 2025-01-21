from fastapi import FastAPI
import uvicorn
from items_views import router as items_router
from users.views import router as users_router
from contextlib import asynccontextmanager
from core.models import Base, db_helper
from api_v1 import router as router_v1
from core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(items_router)
app.include_router(users_router)
app.include_router(
    router=router_v1, prefix=settings.api_v1_prefix
)


@app.get("/")
def hello_money():
    return {
        "message": "FastMoney.com Welcomes you my broke Friend!"
        " So what do you want Here?",
    }


@app.get("/hello/")
def hello(name: str = "Username"):
    name = name.strip().title()
    return {"message": f"Hello, {name}!"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
