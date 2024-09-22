print("Personal Daily Reminder") #app header/tittle

#prompting user inputs for 1. Task, 2 Priority and 3. Time bond

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

Reminder = ""

#evaluations based on user inputs

match priority:
    case "high":
        Reminder += f"Reminder: '{task}' is a {priority} task "
    case "medium":
        Reminder += f"Reminder: '{task}' is a {priority} task. "
    case "low":
        Reminder += f"Note: '{task}' is a {priority} task. "
    case _:
        Reminder += "The priority level is not recognized."
  
if time_bound == "yes":
    Reminder += "that requires immediate attention today!"
if time_bound == "no":
    Reminder += "Consider completing it when you have free time."
print(Reminder)