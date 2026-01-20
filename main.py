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


@app.get("/hello-mesa")
async def hello_mesa():
    return {"message": "Hello, Mesa!"}


@app.get("/hello-cursor")
async def hello_cursor():
    return {"message": "Hello, Cursor!"}


@app.get("/hello-claude")
async def hello_claude():
    return {"message": "Hello, Claude!"}

@app.get("/hello-human")
async def hello_human():
    return {"message": "Hello, Human!"}


@app.get("/hello-agentblame")
async def hello_agentblame():
    return {"message": "Hello, Agentblame!"}


@app.get("/hello-agent")
async def hello_agent():
    return {"message": "Hello, Agent!"}


@app.get("/hello-agent1")
async def hello_agent1():
    return {"message": "Hello, Agent1!"}


@app.get("/hello-abc")
async def hello_abc():
    return {"message": "Hello, ABC!"}


@app.get("/hello-abc1")
async def hello_abc1():
    return {"message": "Hello, ABC1!"}


@app.get("/hello-abc2")
async def hello_abc2():
    return {"message": "Hello, ABC2!"}

@app.get("/hello-abc3")
async def hello_abc3():
    return {"message": "Hello, ABC3!"}
