
import requests
import json

OLLAMA_URL = "http://localhost:11434/api/chat"


def ask_qwen(prompt):

    data = {
        "model": "qwen2.5:1.5b",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": True
    }

    response = requests.post(
        OLLAMA_URL,
        json=data,
        stream=True
    )

    response.raise_for_status()

    print("\nAgent: ", end="", flush=True)

    for line in response.iter_lines():

        if line:
            chunk = json.loads(line)

            content = chunk.get("message", {}).get("content", "")

            print(content, end="", flush=True)

            if chunk.get("done"):
                break

    print()


while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("Agent: Goodbye!")
        break

    ask_qwen(user_input)
