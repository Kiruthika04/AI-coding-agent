from pathlib import Path
from config import client, MODEL_NAME


def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def suggest_changes(file_path, user_request):
    code = read_file(file_path)

    prompt = f"""
You are an expert Node.js developer.

User Request:
{user_request}

File:
{file_path}

Current Code:

{code}

Your task:
1. Explain whether this file needs changes.
2. If yes, provide the updated code.
3. If no changes are needed, reply exactly:
No changes required.
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=1200
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    repo = Path("node-easy-notes-app")

    file_to_check = repo / "app" / "controllers" / "note.controller.js"

    result = suggest_changes(
        str(file_to_check),
        "Improve the application so users can better organise and search their notes."
    )

    print(result)