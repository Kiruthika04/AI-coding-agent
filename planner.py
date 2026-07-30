from config import client, MODEL_NAME
from explorer import explore_repository

def create_plan(repo_path, user_request):
    files = explore_repository(repo_path)

    file_list = "\n".join(files[:100])  # Limit to first 100 files

    prompt = f"""
You are an expert software engineer.

Repository files:

{file_list}

User Request:
{user_request}

Based ONLY on the repository structure above:

1. Brief execution plan
2. Which files should change
3. Why
4. Expected implementation

Do not invent filenames.
Only mention files that exist.
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=400
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    plan = create_plan(
        "node-easy-notes-app",
        "Improve the application so users can better organise and search their notes."
    )

    print(plan)