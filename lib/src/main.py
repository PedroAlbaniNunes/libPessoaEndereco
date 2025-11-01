from fastapi import FastAPI
from util.database import init_db
from controller.pessoa import router as pessoa_router
from controller.endereco import router as endereco_router

app = FastAPI(title="FastAPI+ dtBase + MVC + Repository",
              version="1.1.0",)

init_db()

app.include_router(pessoa_router)
app.include_router(endereco_router)

@app.get("/")
def health():
    return {"Status": "ok" }