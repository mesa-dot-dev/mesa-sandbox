from fastapi import FastAPI
from controllers.items import router as items_router

app = FastAPI(
    title="Mesa Sandbox API",
    description="A basic FastAPI project",
    version="1.0.0",
)

app.include_router(items_router, prefix="/items", tags=["items"])


@app.get("/")
async def root():
    return {"message": "Welcome to Mesa Sandbox API"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


@app.get("/hello-cursor")
async def hello_cursor():
    return {"message": "Hello Cursor"}


@app.get("/hello-claude")
async def hello_claude():
    return {"message": "Hello Claude"}
