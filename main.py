import argparse
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic()

SYSTEM = """You are a response evaluator. Given a task description and a model response, evaluate whether the response meets the task requirements.

Return your evaluation in exactly this format:

VERDICT: pass / fail / partial

REQUIREMENTS:
- [requirement]: met / not met / partial
- [requirement]: met / not met / partial

GAPS:
- [what is missing or wrong]

Be concise. Focus on whether the response actually fulfills what was asked."""

def evaluate(task: str, response: str) -> str:
    message = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=512,
        system=SYSTEM,
        messages=[{
            "role": "user",
            "content": f"TASK:\n{task}\n\nRESPONSE:\n{response}"
        }]
    )
    return message.content[0].text

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate a model response against a task.")
    parser.add_argument("--task", required=True, help="The task description")
    parser.add_argument("--response", required=True, help="The model response to evaluate")
    args = parser.parse_args()
    print(evaluate(args.task, args.response))