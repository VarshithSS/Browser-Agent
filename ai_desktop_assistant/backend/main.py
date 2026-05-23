import sys
import asyncio

if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(
        asyncio.WindowsProactorEventLoopPolicy()
    )

from fastapi import FastAPI
from pydantic import BaseModel

from tools.tool_registry import browser
from agent.llm_agent import run_agent

app = FastAPI()


class UserRequest(BaseModel):
    task: str


@app.on_event("startup")
async def startup_event():
    await browser.start()


@app.post("/agent")
async def agent_endpoint(request: UserRequest):

    result = await run_agent(request.task)

    return result