print("Personal Daily Reminder") #app header/tittle

#prompting user inputs for 1. Task, 2 Priority and 3. Time bond

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

#evaluating cases based on users inputs
match priority:
    case "high" | "medium" | "low":
        if time_bound == "yes":
            print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
        else:
            if time_bound == "no":
                print(f"Note: {task} is a {priority} priority task. Consider completing it when you have free time.")
    case _ :
        print("I dont have a reminder or time bond for your request")