# daily_reminder.py

# Prompt for a single task
task = input("Enter your task for today: ")
priority = input("Enter the task's priority (high/medium/low): ").lower()
time_bound = input("Is the task time-bound? (yes/no): ").lower()

# Provide customized reminder
print("\n--- Daily Reminder ---")

match priority:
    case "high":
        message = f"Your high-priority task: '{task}'."
    case "medium":
        message = f"Your medium-priority task: '{task}'."
    case "low":
        message = f"Your low-priority task: '{task}'."
    case _:
        message = f"Your task: '{task}' (unknown priority)."

if time_bound == "yes":
    message += " This task requires immediate attention today!"

print(message)
