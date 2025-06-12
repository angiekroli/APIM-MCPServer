from fastapi import FastAPI
from container.routes import router

def create_app() -> FastAPI:
    app = FastAPI(title="PokeAPI Proxy")
    app.include_router(router)
    return app

app = create_app()
