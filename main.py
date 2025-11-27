from manager.task_manager import TaskManager

def main():
    print("=== Multi-Agent Capstone Project ===")

    topic = input("Enter your project topic: ")

    manager = TaskManager()
    results = manager.run_pipeline(topic)

    print("\n=== FINAL OUTPUT ===")
    for stage, output in results.items():
        print(f"\n--- {stage.upper()} AGENT RESULT ---")
        for key, value in output.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    main()
