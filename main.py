# src/main.py

import argparse
import json
import yaml
import sys
from pathlib import Path


def load_config(config_path: str) -> dict:
    """Load YAML configuration file."""
    with open(config_path, "r") as f:
        return yaml.safe_load(f)


def load_input(input_path: str) -> dict:
    """Load JSON input file."""
    with open(input_path, "r") as f:
        return json.load(f)


def run_agent(config: dict, user_input: dict):
    """
    Dummy agent runner.
    Replace this with your actual agent pipeline using langgraph / LLMs.
    """
    # Example: just echoing back
    return {
        "status": "success",
        "message": "Agent executed successfully",
        "config_used": config.get("name", "default"),
        "input_received": user_input,
        "response": f"Processed: {user_input.get('query', 'No query found')}"
    }


def main():
    parser = argparse.ArgumentParser(description="Run the LangGraph Agent")
    parser.add_argument("--config", required=True, help="Path to YAML config file")
    parser.add_argument("--input", required=True, help="Path to JSON input file")
    args = parser.parse_args()

    # Load config + input
    config = load_config(args.config)
    user_input = load_input(args.input)

    # Run the agent
    result = run_agent(config, user_input)

    # Print result to console as JSON
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
