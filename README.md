# AI Coding Agent

## Overview

This project is an AI-powered coding agent that explores a Node.js repository, analyzes the codebase, creates an execution plan, and generates code modification suggestions using an LLM.

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

## Workflow

1. Explore the repository.
2. Analyze the repository structure.
3. Generate an execution plan.
4. Identify relevant files.
5. Generate AI-powered code suggestions.
6. Save suggestions to the `generated_changes` folder.

## Assumptions

- The repository is a Node.js application.
- The LLM has sufficient context to analyze individual files.
- Suggested changes are reviewed before being applied.

## Future Improvements

- Automatically modify files.
- Generate Git patches.
- Support multiple programming languages.
- Add rollback functionality.