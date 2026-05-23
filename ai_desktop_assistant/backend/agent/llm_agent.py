import json

from llm.groq_client import get_llm_response
from tools.tool_registry import TOOLS
from agent.prompts import SYSTEM_PROMPT


async def run_agent(user_input: str):

    prompt = f"""
{SYSTEM_PROMPT}

User Request:
{user_input}
"""

    response = await get_llm_response(prompt)

    print("\nLLM RESPONSE:\n", response)

    action = json.loads(response)

    # Extract values FIRST
    tool_name = action["tool"]
    args = action["args"]

    # Handle unsupported actions
    if tool_name == "unsupported":

        return {
            "status": "unsupported",
            "reason": args["reason"]
        }

    # Execute valid tool
    tool = TOOLS[tool_name]["func"]

    result = await tool(**args)

    return {
        "tool_used": tool_name,
        "result": result
    }