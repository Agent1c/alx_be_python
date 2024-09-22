print("Personal Daily Reminder") #app header/tittle

#prompting user inputs for 1. Task, 2 Priority and 3. Time bond

task = input("Enter your task: ").lower()
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

reminder = ""

#evaluations based on user inputs

match priority:
    case "high":
        reminder += f"'{task}' is a {priority} priority task "
    case "medium":
        reminder += f"'{task}' is a {priority} priority task"
    case "low":
        reminder += f"'{task}' is a {priority} priority task."
    case _:
        reminder += "The priority level is not recognized."
  
if time_bound == "yes":
    print(f"Reminder: {reminder}that requires immediate attention today!")
else:
    print(f"Note: {reminder} Consider completing it when you have free time.")
# print(reminder)