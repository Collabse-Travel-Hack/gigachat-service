from fastapi import FastAPI
from routers.prompts import router


app = FastAPI()
app.include_router(router)