## Capstone Project — Automated ML Multi-Agent System

A submission for the Google × Kaggle 5-Day Agents Capstone

Project Overview

Traditional machine learning workflows require manual repetition of tasks like:
1. data loading
2. cleaning
3. feature engineering
4. training multiple models
5. evaluating performance
6. creating reports

This project automates the entire ML pipeline using a multi-agent architecture powered by LLM reasoning.

The system uses four cooperating agents, each handling a distinct step.
This improves:

1.reproducibility
2.automation
3.speed
4.reliability

🧠 Why Agents?

Agents are ideal because ML workflows are:

modular (different tasks)

repeatable

sequenced (A → B → C → D)

data-dependent

Using multiple agents allows:

task specialization

parallelization (optional)

clearer separation of responsibilities

better observability

🔧 Agents Included
1️⃣ DataAgent

Handles:

loading the dataset

preprocessing

label encoding

handling missing values

2️⃣ TrainingAgent

Responsible for:

splitting data

selecting ML algorithms

training models

3️⃣ EvaluationAgent

Performs:

model prediction

accuracy computation

classification metrics

analysis of errors

4️⃣ ReportAgent

Creates:

1.feature importance charts
2.final report assets
3.visual outputs for submission

🏗️ Architecture
              ┌──────────────────┐
              │   DataAgent       │
              │ Load + Preprocess │
              └─────────┬────────┘
                        │
                        ▼
             ┌────────────────────┐
             │   TrainingAgent     │
             │ Train ML Model      │
             └─────────┬──────────┘
                       │
                       ▼
          ┌─────────────────────────┐
          │     EvaluationAgent      │
          │ Accuracy + Classification│
          └───────────┬─────────────┘
                      │
                      ▼
            ┌──────────────────────┐
            │    ReportAgent        │
            │   Graphs + Summary    │
            └──────────────────────┘
📚 Tech Stack

1.Python 3.10+
2.Pandas (data handling)
3.NumPy (numeric operations)
4.Scikit-Learn (models)
5.Matplotlib (visual reports)

repository structure
capstone-ai-agent/
│── README.md
│── requirements.txt
│── orchestrator.py
│
│── agents/
│   │── data_agent.py
│   │── training_agent.py
│   │── evaluation_agent.py
│   │── report_agent.py
│
│── data/
│   └── dataset.csv
│
│── models/
│── reports/

🚀 How to Run
Step 1: Install requirements
pip install -r requirements.txt

Step 2: Place your dataset
data/dataset.csv

Step 3: Run the main orchestrator
python orchestrator.py

Manual ML pipelines are slow and require repeated human effort.
my solution automates:
✔ cleaning
✔ training
✔ evaluating
✔ reporting

This reduces time from hours to minutes.
