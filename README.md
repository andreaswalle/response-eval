# response-eval

Evaluates model responses against task requirements.

Given a task and a response, `response-eval` checks whether the response
actually fulfills what was asked — identifying unmet requirements and gaps.

## Usage

```bash
python main.py --task "Write a Python function that returns the sum of two numbers." \
               --response "def add(a, b): return a + b"
```

Output:

```
VERDICT: pass

REQUIREMENTS:
- Function returns the sum of two numbers: met
- Function is written in Python: met
- Function is syntactically correct: met

GAPS:
- None
```

## Why

Task clarity is necessary but not sufficient. A well-formed task can still
produce a response that misses the point. This tool makes that visible —
systematically, before human review.

Pairs with [task-clarity](https://github.com/andreaswalle/task-clarity):
task-clarity checks the task, response-eval checks the answer.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# add your Anthropic API key to .env
python main.py --task "your task" --response "model output"
```

## Requirements

- Python 3.9+
- Anthropic API key