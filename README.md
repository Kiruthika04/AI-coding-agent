# AI Coding Agent

## Overview

This project is an AI-powered coding agent that explores a Node.js repository, analyzes the codebase, creates an execution plan, and generates code modification suggestions using an LLM.

## Architecture

```text
                User Request
                     │
                     ▼
            +----------------+
            |    agent.py    |
            | Main Controller|
            +----------------+
                     │
     ┌───────────────┼───────────────┐
     ▼               ▼               ▼
+------------+  +------------+  +-------------+
| explorer.py|  | planner.py |  | modifier.py |
+------------+  +------------+  +-------------+
        │             │               │
        └─────────────┼───────────────┘
                      ▼
       +-------------------------------+
       | generated_changes/*.md        |
       +-------------------------------+
```

## Features

- Repository exploration
- AI-generated execution planning
- Code analysis
- AI-generated code suggestions
- Saves generated suggestions into Markdown files

## Project Structure

```
ai-coding-agent/
├── agent.py
├── config.py
├── explorer.py
├── planner.py
├── modifier.py
├── utils.py
├── generated_changes/
├── node-easy-notes-app/
├── requirements.txt
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_api_key
MODEL_NAME=qwen/qwen3-coder
```

## Run

```bash
python agent.py
```

## Agent Workflow

1. User provides a feature request.

2. explorer.py scans the repository and collects relevant source files.

3. planner.py creates an implementation plan using the LLM.

4. modifier.py analyzes important files individually and generates code suggestions.

5. Suggestions are saved into the generated_changes folder as Markdown files.

6. agent.py orchestrates the complete workflow.

## Repository Exploration

The repository is explored using Python's `os.walk()`.

The explorer:

- Recursively scans the project directory
- Ignores unnecessary folders:
  - node_modules
  - .git
  - __pycache__
  - venv
- Collects relevant source files
- Passes the file list to the planner so the LLM only analyzes existing project files.

## Assumptions

- The repository is a Node.js application.
- The LLM has sufficient context to analyze individual files.
- Suggested changes are reviewed before being applied.

## Assumptions

- The repository follows a standard project structure.
- The user request is clear and specific.
- The LLM has enough context to analyze individual files.

## Trade-offs

- The agent generates suggestions instead of automatically editing files.
- File analysis is performed one file at a time to reduce prompt size.
- Generated changes should be reviewed before applying.

## Example Output

The generated suggestions are saved inside:

generated_changes/

Example:

generated_changes/
├── note.controller.md
├── note.model.md
└── note.routes.md

## Technologies

- Python
- OpenRouter API
- Qwen Coder Model
- dotenv
- pathlib

## Future Improvements

- Automatically modify files.
- Generate Git patches.
- Support multiple programming languages.
- Add rollback functionality.
