print("Personal Daily Reminder") #app header/tittle

#prompting user inputs for 1. Task, 2 Priority and 3. Time bond

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

reminder = ""

#evaluations based on user inputs

match priority:
    case "high":
        reminder += f"Reminder: '{task}' is a {priority} task "
    case "medium":
        reminder += f"Reminder: '{task}' is a {priority} task. "
    case "low":
        reminder += f"Note: '{task}' is a {priority} task. "
    case _:
        reminder += "The priority level is not recognized."
  
if time_bound == "yes":
    reminder += "that requires immediate attention today!"
if time_bound == "no":
    reminder += "Consider completing it when you have free time."
print(reminder)