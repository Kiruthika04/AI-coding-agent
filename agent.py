from explorer import explore_repository
from planner import create_plan
from modifier import suggest_changes
from pathlib import Path

REPO_PATH = "node-easy-notes-app"

USER_REQUEST = (
    "Improve the application so users can better organise and search their notes."
)

print("=" * 60)
print("AI Coding Agent")
print("=" * 60)

print("\nStep 1: Exploring repository...")
files = explore_repository(REPO_PATH)
print(f"Found {len(files)} files.")

print("\nStep 2: Creating execution plan...")
plan = create_plan(REPO_PATH, USER_REQUEST)
print(plan)

print("\nStep 3: Analyzing important files...")

important_files = [
    "app/controllers/note.controller.js",
    "app/models/note.model.js",
    "app/routes/note.routes.js",
]

for file in important_files:
    path = Path(REPO_PATH) / file

    if path.exists():
        print(f"\n--- {file} ---")

        result = suggest_changes(str(path), USER_REQUEST)

        # Create output folder
        output_dir = Path("generated_changes")
        output_dir.mkdir(exist_ok=True)

        # Save AI response
        output_file = output_dir / f"{path.stem}.md"

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result)

        print(f"Saved: {output_file}")

    else:
        print(f"{file} not found.")

print("\nAnalysis complete!")