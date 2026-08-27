from configs import MAX_TURNS
from client import get_client_and_model
from prompts.prompt_loader import build_system_prompt
from schemas import TOOLS_MENU
from tools import TOOL_FUNCTIONS
import json

def run_agent_turns(messages: str, max_turns: int = MAX_TURNS) -> str:
    client, model, _ = get_client_and_model()

    working = [
        {
            "role": "system",
            "content": build_system_prompt(),
        },
        *messages
    ]

    for _ in range(max_turns):
        response = client.chat.completions.create(
            model=model,
            messages=working,
            tools=TOOLS_MENU,
        )

        message = response.choices[0].message

        # Final Answer

        if not message.tool_calls:
            answer = message.content or ""

            messages.append({
                "role": "assistant",
                "content": answer
            })
            return answer

        # Add asssistant tool calls

        working.append({
            "role": "assistant",
            "content": message.content,
            "tool_calls": [
                {
                    "id": call.id,
                    "type": "function",
                    "function": {
                        "name": call.function.name,
                        "arguments": call.function.arguments,
                    }
                } for call in message.tool_calls
            ]
        })

        # Execute tools
        for call in message.tool_calls:
            name = call.function.name

            if name not in TOOL_FUNCTIONS:
                tool_result = f"Unknown tool: {name}"

            else:
                try:
                    arguments = json.loads(call.function.arguments)

                    tool_result = TOOL_FUNCTIONS[name](**arguments)

                except Exception as e:
                    tool_result = f"Tool execution error: {e}"

            working.append({
                "role": "tool",
                "content": str(tool_result),
                "tool_call_id": call.id
            })

    fallback = "Stopped after hitting the max_turns without a final answer"

    messages.append({
        "role": "assistant",
        "content": fallback
    })

    return fallback

def start_agent():
    prompt = input("Enter prompt: ")

    user_prompt = [{
        "role": "user",
        "content": prompt
    }]

    answer = run_agent_turns(messages=user_prompt)

    print(answer)

start_agent()