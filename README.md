## Multi-Agent DevBot — Google × Kaggle Capstone Project

1. Introduction
This project is my submission for the Google × Kaggle 5-Day Generative AI Agents Course Capstone.
I built a simple multi-agent system that can help with software development tasks such as researching a topic, drafting basic code, and testing the generated code.
The idea is to show how different agents can work together, each handling one responsibility.

The project is created using Python and follows the concepts taught in the course.

2. Problem Statement
When we start working on a new programming task, we usually repeat the same steps:

Search the internet
Collect useful points
Draft some initial code
Check if the code works

Doing all this manually every time can be slow. So the aim here is to automate the first version of this process. Not to replace developers, but to help save time in the early stages.

3. Proposed Solution
The solution is a simple multi-agent system with three agents:

1. Research Agent
Takes a topic and produces a small research summary (simulated).

2. Coding Agent
Uses the research result to generate a basic Python function.

3. Testing Agent
Runs checks to ensure the generated code does not crash.

All three are connected through a manager that sends the output of one agent to the next.

4. Architecture Overview
User Input
    ↓
Research Agent
    ↓
Coding Agent
    ↓
Testing Agent
    ↓
Final Output

Each agent is a separate Python module, and the manager coordinates the workflow step-by-step.

5. Features Implemented (as required by Capstone)
✔ Multi-Agent Syste
Three agents working in a sequence, each with a narrow role.
✔ Tools
A simulated web search tool
A simple code quality checker
✔ Session / State Flow
The output moves from one agent to another in a controlled order.
✔ Observability
Each step prints what it’s doing so it’s clear how the system is working.

6. Folder Structure
multi-agent-dev-bot/
│
├── main.py
├── README.md
│
├── agents/
│   ├── research_agent.py
│   ├── coding_agent.py
│   ├── testing_agent.py
│   └── __init__.py
│
├── manager/
│   ├── task_manager.py
│   └── __init__.py
│
└── utils/
    ├── tools.py
    └── __init__.py

7. How It Works (Simple Explanation)

The user types a topic.
Research Agent prepares a short “research-like” summary.
Coding Agent writes a basic Python function using that summary.
Testing Agent runs the code safely.
Everything is printed clearly at the end.
This is not meant to create perfect code — just to demonstrate how agents can work together.

8. Running the Project
Step 1: Clone the repo
git clone https://github.com/<your-username>/multi-agent-dev-bot.git
cd multi-agent-dev-bot

Step 2: Run
python main.py


No API keys or external setups are needed.

9. Example Output
=== Multi-Agent Workflow ===
Research Agent researching topic...
Coding Agent generating code...
Testing Agent running tests...

FINAL OUTPUT:
Research Summary: ...
Generated Code: ...
Testing Result: All tests passed.

10. Why This Project Is Useful

Demonstrates understanding of multi-agent systems.
Easy to extend into more complex agents later.
Works offline and requires no paid models.
Good starting point for experimenting with agent workflows.

11. Future Improvements

If I expand this later, I may add:
Real web search tools
Better code generation
Deployment using Cloud Run

A dashboard UI

A short YouTube demo video for bonus marks

12. Author

BUVAN R
Google × Kaggle Generative AI Agents Course
2025

 GitHub project

 Under 1500 words
