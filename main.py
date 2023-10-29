from fastapi import FastAPI
from routers.route import router

app=FastAPI()
app.include_router(router)