from fastapi import FastAPI
from api.rest import router


app = FastAPI(title="Task Api", docs_url="/", version="1.0.0")

app.include_router(
    router,
    prefix="/task",
    tags=["Task"],
)
