import os

IGNORE_DIRS = {
    ".git",
    "node_modules",
    "__pycache__",
    "venv"
}


def explore_repository(repo_path):
    files = []

    for root, dirs, filenames in os.walk(repo_path):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        for file in filenames:
            path = os.path.join(root, file)
            files.append(path)

    return files


if __name__ == "__main__":
    repo = "node-easy-notes-app"

    files = explore_repository(repo)

    print(f"\nFound {len(files)} files\n")

    for f in files:
        print(f)