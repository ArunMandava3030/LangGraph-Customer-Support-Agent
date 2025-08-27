# LangGraph-Customer-Support-Agent

This project is a Customer Support Agent built using LangGraph, LangChain, and Hugging Face models. It was developed as part of the Slooze Take-Home Challenge (Data Engineering). The goal is to demonstrate how a lightweight conversational agent can process customer support queries by combining structured input, configuration-driven setup, and modular components.

📌 Project Overview

Framework: Built with LangGraph
 and LangChain
.

Model: Uses a Hugging Face transformers pipeline (local model) for text generation.

Configurable: Agent behavior can be controlled via YAML configuration files.

Input Handling: Accepts structured JSON inputs for customer queries.

Output: Returns a structured JSON response with query, status, and agent output.

This project demonstrates Part A & B of the challenge requirements:

Data Collection / Scraping: Not applicable here (since this is the AI agent portion).

Agent Implementation: ✅ Completed with LangGraph + Hugging Face.

Config-driven Execution: ✅ Uses config/agent.yaml to control behavior.

Test Input Handling: ✅ Runs with tests/demo_input.json.

📂 Project Structure
langgraph-cs-agent/
│── config/
│   └── agent.yaml            # Agent configuration file
│
│── src/
│   ├── __init__.py
│   ├── main.py               # Entry point for running the agent
│   └── agent.py              # Defines the CustomerSupportAgent
│
│── tests/
│   └── demo_input.json       # Example input query
│
│── requirements.txt          # Python dependencies
│── README.md                 # Project documentation (this file)

⚙️ Setup Instructions

Clone the repo

git clone https://github.com/ArunMandava3030/Slooze_challenge_data-engineering.git
cd Slooze_challenge_data-engineering/langgraph-cs-agent


Create a virtual environment

python -m venv .venv
source .venv/bin/activate     # Mac/Linux
.venv\Scripts\activate        # Windows


Install dependencies

pip install -r requirements.txt

▶️ Running the Agent

You can run the agent using the following command:

python -m src.main --config config/agent.yaml --input tests/demo_input.json

✅ Example Output
{
  "status": "success",
  "message": "Agent executed successfully",
  "config_used": "default",
  "input_received": {
    "query": "Show me all customers who placed an order in the last 7 days"
  },
  "response": "Processed: Show me all customers who placed an order in the last 7 days"
}

🧪 Testing with Custom Inputs

Modify tests/demo_input.json with your own query, for example:

{
  "query": "List all pending support tickets for customer ID 12345"
}


Then rerun:

python -m src.main --config config/agent.yaml --input tests/demo_input.json

✅ Task Requirements Check

Agent implemented with LangGraph → Done in src/agent.py.

Configuration file provided (YAML) → config/agent.yaml.

Input/Output handling with JSON → tests/demo_input.json.

Modular code structure → src/ package with agent.py and main.py.

Execution with CLI commands → python -m src.main.

Example run + output included → Documented above.

![alt text](https://github.com/ArunMandava3030/LangGraph-Customer-SupportAgent/blob/bd81a999683e5fd37f39c255076deb9abdcae8c5/Screenshot%202025-08-27%20223922.png)

![alt text](https://github.com/ArunMandava3030/LangGraph-Customer-SupportAgent/blob/bd81a999683e5fd37f39c255076deb9abdcae8c5/Screenshot%202025-08-27%20223953.png)
