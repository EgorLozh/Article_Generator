from config import LLAMA_API_TOKEN
import json

from llamaapi import LlamaAPI


def send_message():
    llama = LlamaAPI(LLAMA_API_TOKEN)

    api_request_json = {
        "messages": [
            {"role": "user", "content": "What is the weather like in Boston?"},
        ],
        "functions": [
            {
                "name": "get_current_weather",
                "description": "Get the current weather in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA",
                        },
                        "days": {
                            "type": "number",
                            "description": "for how many days ahead you wants the forecast",
                        },
                        "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                    },
                },
                "required": ["location", "days"],
            }
        ],
        "stream": False,
        "function_call": "get_current_weather",
    }

    response = llama.run(api_request_json)
    print(response.text)

send_message()
