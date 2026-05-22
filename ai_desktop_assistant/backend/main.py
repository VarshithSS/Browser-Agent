import asyncio

asyncio.set_event_loop_policy(
    asyncio.WindowsSelectorEventLoopPolicy()
)

from fastapi import FastAPI
from pydantic import BaseModel

from agent.simple_agent import (
    run_agent,
    initialize_browser
)

app = FastAPI()


class Query(BaseModel):
    message: str


@app.on_event("startup")
async def startup_event():
    await initialize_browser()


@app.post("/chat")
async def chat(query: Query):

    response = await run_agent(query.message)

    return {
        "response": response
    }










