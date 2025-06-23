import os
import time
import random
import datetime

def currentDate():
    
    """Returns the current date.

    Uses the datetime module to get the current system date 
    and returns it in YYYY-MM-DD format.

    Returns:
        date (datetime.date): The current date """
    
    now = datetime.datetime.now()
    date = now.date()
    return date

def threeDaysBeforeDate():
    
    """Returns the date that is three days before the current date.

    Calculates the date by subtracting three days from today's date 
    using the datetime module.

    Returns:
        date (datetime.date): The date three days before today."""
    
    specific_date = datetime.datetime.now()
    three_days_before = specific_date - datetime.timedelta(days=3)
    return three_days_before.date()

def signUp():
    
    """Handles user signup for the Study Assistant.

    - Prompts the user for their name and class (only if "User Info.txt" does not exist).
    - Saves the entered name, class, and the current signup date in "User Info.txt".
    - If "Coins.txt" does not exist, it creates the file and initializes the user's coin balance to 0.

    This function ensures user data is created only once, and is reused across sessions."""
    
    if not os.path.exists("User Info.txt"):
        print("Signup to save your tasks and progress\n")
        entered_name = input("Enter you name: ")

        while True:
            try:
                entered_class = int(input("In which class are you studying: "))
                break
            except Exception as e:
                print(f"Sorry!Some error occurred\nError: {e}")

        signup_time = currentDate()

        with open("User Info.txt", "w") as ui:
            ui.write(f"{entered_name}\n{entered_class}\n{signup_time}")

    if not os.path.exists("Coins.txt"):
        with open("Coins.txt", "w") as c:
            c.write("0")

def signingSubjects():
    
    """Initializes the subjects and their syllabus for the user.

    - Creates a "Subjects" directory if it does not already exist.
    - Asks the user how many subjects they have.
    - For each subject, prompts the user to enter the subject name and total number of chapters.
    - Saves this data in a separate file for each subject inside the "Subjects" directory.
      Each file contains two lines:
        1. Total number of chapters
        2. Chapters completed (initially 0)

    Skips creating a file if the subject is already recorded."""
    
    if not os.path.exists("Subjects"):
        os.mkdir("Subjects")

        while True:
            try:
                subjectsNum = int(input("\nHow many subjects do you have? "))
                break
            except Exception as e:
                print(f"Sorry!! Some error occurred.\nError: {e}")

        for i in range(1, subjectsNum + 1):
            subject = input(f"Enter subject {i}: ")
            chapters = input(f"Enter the number of chapters in {subject}: ")

            if not os.path.exists(f"Subjects/{subject}.txt"):
                with open(f"Subjects/{subject}.txt", "w") as s:
                    s.write(f"{chapters}\n0")
            else:
                print("You have already given this subject")

def filterTasks(task):
    
    """ Filters out completed tasks that are older than 3 days.

    If a task is incomplete (not marked with [✅]), it is always kept.
    If a task is completed, it checks the due date and removes it if it's
    3 or more days old.

    Args:
        task (str): A string representing a task line from the task file.

    Returns:
        bool: True if the task should be kept, False if it should be removed. """
    
    if not task.startswith("[✅]"):
        return True 

    try:
        due_date_str = task.split("Due: ")[-1].strip()
        due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d").date()
        today = datetime.date.today()
        return (today - due_date).days < 3
    except Exception as e:
        print(f"⚠️ Error filtering task: {e}")
        return True

def addTasks():
    
    """Adds a new task to the task list.

    - Prompts the user to enter the subject and task title.
    - Automatically assigns the current date as the due date.
    - Appends the task to "Tasks.txt" in the following format:
        [🕒] Task Title (Subject) - Due: YYYY-MM-DD
    - Displays a success message after adding the task.

    This function helps the user keep track of pending tasks with a timestamp."""
    
    subject = input("\nSubject: ")
    task = input("Task title: ")
    dueDate = currentDate()
    print(f"Due Date (YYYY-MM-DD): {dueDate}")

    with open("Tasks.txt", "a") as t:
        t.write(f"[🕒] {task} ({subject}) - Due: {dueDate}\n")

    time.sleep(2)
    print("\n✅ Task added successfully!")

def viewTasks():
   
    """Displays all tasks currently stored in "Tasks.txt".

    - Checks if the "Tasks.txt" file exists.
    - If it does, reads and prints each task with a serial number.
    - If the file doesn't exist or is empty, informs the user that there are no tasks.
    - Returns True if tasks were found and displayed, otherwise returns False.

    This function helps the user view their current pending and completed tasks. """
    
    if os.path.exists("Tasks.txt"):
        with open("Tasks.txt", "r") as t:
            tasks = t.read().splitlines()

        print("\n📋 Your Tasks: \n")
        for index, task in enumerate(tasks):
            print(f"{index + 1}.{task}")
        return True
    else:
        print("No Tasks! ")
        return False

def taskDone():
    
    """Marks a selected task as completed and rewards the user with coins.

    - Displays the list of current tasks using the `viewTasks()` function.
    - Prompts the user to select a task number to mark as done.
    - Replaces the task's status from "[🕒]" (pending) to "[✅]" (completed).
    - Updates the "Tasks.txt" file with the modified task list.
    - Randomly rewards the user with coins (between 5 to 50, only if divisible by 5).
    - Updates the "Coins.txt" file with the new coin balance.
    - Shows confirmation messages and the updated coin total.

    Helps the user keep track of completed work and stay motivated through rewards. """
    
    print("Which task would you like to mark as done? ")
    tasksExist = viewTasks()

    if tasksExist:
        with open("Tasks.txt", "r") as t:
            tasks = t.read().splitlines()

        while True:
            try:
                serialNum = int(input("\nEnter the task number to mark as done: "))
                completedTask = tasks[serialNum - 1]
                newTask = completedTask.replace("[🕒]", "[✅]")
                tasks.remove(completedTask)
                tasks.append(newTask)

                with open("Tasks.txt", "w") as t:
                    t.write("")

                for task in tasks:
                    with open("Tasks.txt", "a") as t:
                        t.write(task + "\n")
                print("\n✅ Task marked as completed. ")

                while True:
                    coinsWon = random.randint(5, 50)
                    if coinsWon % 5 == 0:
                        with open("Coins.txt", "r") as c:
                            prevCoins = int(c.read())
                        totalCoins = coinsWon + prevCoins
                        with open("Coins.txt", "w") as c:
                            c.write(str(totalCoins))
                        print(f"🎉 You earned {coinsWon} coins!")
                        print(f" Current Balance: {totalCoins} coins")
                        break

                break

            except Exception as e:
                print(f"Sorry! Some error occurred! \nError: {e}")

def completedTask(task):
    """Checks if a task is marked as completed.

    Args:
        task (str): The task string to check.

    Returns:
        str or None: Returns the task if it is marked as completed with [✅], otherwise None."""
    if (task.split(" ")[0] == "[✅]"):
        return task

def incompleteTask(task):
    """Checks if a task is still incomplete.

    Args:
        task (str): The task string to check.

    Returns:
        str or None: Returns the task if it is marked as incomplete with [🕒], otherwise None """
    if (task.split(" ")[0] == "[🕒]"):
        return task

def taskProgress():
    
    """Displays the overall progress of tasks.

    - Reads all tasks from "Tasks.txt".
    - Filters the list into completed and incomplete tasks using the `completedTask()` and `incompleteTask()` functions.
    - Calculates the percentage of tasks completed.
    - Prints the count of completed and pending tasks, along with the completion percentage (rounded to two decimal places).

    This function provides a quick overview of the user's productivity and task completion rate. """
    
    print("\n📊 Task Progress:")

    with open("Tasks.txt", "r") as t:
        tasks = t.read().splitlines()

    completeTasks = list(filter(completedTask, tasks))
    incompleteTasks = list(filter(incompleteTask, tasks))
    completionProgress = (len(completeTasks) / len(tasks)) * 100

    print(f"✔️ Done: {len(completeTasks)}")
    print(f"⌛ Pending: {len(incompleteTasks)}")
    print(f"📈 Completion: {completionProgress:.2f} %")

def skipTask():

    """Allows the user to skip a task by spending 10 coins.

    - Displays all current tasks using `viewTasks()`.
    - Prompts the user to select the task number they want to skip.
    - Checks if the user has at least 10 coins.
    - If enough coins are available:
        - Removes the selected task from the task list.
        - Deducts 10 coins from the user's balance.
        - Updates both "Tasks.txt" and "Coins.txt" accordingly.
        - Confirms the task skip and shows the updated coin balance.
    - If not enough coins are available, notifies the user.
    - Handles any input or file-related errors gracefully.

    This function provides users with the flexibility to skip tasks at the cost of virtual coins. """
    
    taskExist = viewTasks()

    if taskExist:
        with open("Tasks.txt", "r") as t:
            tasks = t.read().splitlines()

        with open("Coins.txt", "r") as c:
            coins = int(c.read())

        while True:
            try:
                print("\n🪙 Coins required to skip a task: 10")
                skippedTask = int(input("Enter the Serial number of task which you would like to skip: "))
                tasks.remove(tasks[skippedTask - 1])
                fCoins = coins - 10
                if fCoins >= 0:
                    print(f"✅ Task skipped\nCurrent Balance: {fCoins}")
                    with open("Coins.txt", "w") as c:
                        c.write(str(fCoins))
                    break
                else:
                    print("You don't have coins to skip a task")
            except Exception as e:
                print(f"Sorry! Some error occurred!\nError: {e}")

        with open("Tasks.txt", "w") as t:
            t.write("")

        for task in tasks:
            with open("Tasks.txt", "a") as t:
                t.write(task + "\n")

def syllabusTracker():
    
    """Allows the user to manage and track syllabus progress for different subjects.

    Features:
    1. ✅ Mark Chapters as Covered:
        - Prompts the user to enter the subject name and number of chapters completed.
        - Updates the respective subject file with the completed chapter count.
        - Each subject file is expected to have two lines:
            Line 1: Total chapters
            Line 2: Chapters completed

    2. 📊 Show Progress:
        - Reads all subject files from the "Subjects" directory.
        - Calculates and displays the completion percentage for each subject.

    3. 🔙 Back to Main Menu:
        - Exits the syllabus tracker and returns control to the main menu.

    Ensures subjects are already initialized using `signingSubjects()` before use.
    Helps students stay on top of their syllabus with a visual progress tracker. """
    
    print("\n📘 Welcome to Syllabus Tracker\n")

    options = ["✅ Mark Chapters as Covered", "📊 Show Progress", "🔙 Back to Main Menu"]

    for index, option in enumerate(options):
        print(f"{index + 1}. {option}")

    while True:
        try:
            choice = int(input("\nChoose: "))

            if choice == 1:
                subject = input("Choose Subject: ").strip()

                if os.path.exists(f"Subjects/{subject}.txt"):
                    completedChapters = int(input("Chapters completed now: "))

                    with open(f"Subjects/{subject}.txt", "r") as s:
                        totalChapters = s.read().splitlines()[0]

                    with open(f"Subjects/{subject}.txt", "w") as s:
                        s.write(f"{totalChapters}\n{completedChapters}")

                    print(f"✅ Updated! You’ve now completed {completedChapters}/{totalChapters} chapters. ")

                else:
                    print("Oops! That subject is not in your list 📚❌")

            elif choice == 2:
                files = os.listdir("Subjects")
                print("\n📚 Syllabus Progress:\n")

                for index, file in enumerate(files):
                    subject = file.split(".")[0]
                    with open(f"Subjects/{file}", "r") as s:
                        allChapters = s.read().splitlines()
                        totalChapters = int(allChapters[0])
                        completedChapters = int(allChapters[1])
                        percentage = (completedChapters / totalChapters) * 100

                        print(f"{index + 1}. {subject}: {percentage:.2f} % ✅ ({completedChapters} of {totalChapters} chapters)")

            elif choice == 3:
                break

            else:
                print("Kindly enter a valid number. ")

        except Exception as e:
            print(f"Sorry! Some error occurred.\nError: {e}")

def main():
   
    """Main function to run the Study Assistant application.

    Responsibilities:
    - Displays a welcome message.
    - Calls sign-up and subject setup functions if it's the first run.
    - Loads and filters tasks, removing completed tasks older than 3 days.
    - Loads the current coin balance.
    - Displays the main menu and handles user choices:
        1. Add Task
        2. View Tasks
        3. Mark Task as Done
        4. Show Task Progress
        5. Skip a Task (deducts coins)
        6. Syllabus Tracker (track and update subject progress)
        7. Save & Exit
    - Gracefully handles input errors and exceptions."""
    
    print("📚 Welcome to Study Assistant")
    signUp()
    signingSubjects()

    if not os.path.exists("Tasks.txt"):
        open("Tasks.txt", "w").close()

    with open("Tasks.txt", "r") as t:
        tasks = t.read().splitlines()

    newTasks = list(filter(filterTasks, tasks))

    with open("Tasks.txt", "w") as t:
        t.write("")

    for task in newTasks:
        with open("Tasks.txt", "a") as t:
            t.write(task + "\n")

    print("Loading saved data...")
    time.sleep(3)

    with open("Coins.txt", "r") as c:
        coins = int(c.read())

    print(f"\n📂 Tasks and syllabus loaded.\n🪙 You currently have {coins} coins.")
    time.sleep(2)
    print("\n============ Main Menu ============\n")

    menu = [
        "➕ Add Task", 
        "📋 View Tasks", 
        "✅ Mark Task as Done", 
        "📊 Show Task Progress",
        "⛷️ Skip a Task", 
        "📘 Syllabus Tracker", 
        "💾 Save & Exit"
    ]

    for i, m in enumerate(menu):
        print(f"{i + 1}. {m}")
    print("\n===================================")

    while True:
        try:
            choice = int(input("\nChoose an option: "))

            if choice == 1:
                addTasks()
            elif choice == 2:
                viewTasks()
            elif choice == 3:
                taskDone()
            elif choice == 4:
                taskProgress()
            elif choice == 5:
                skipTask()
            elif choice == 6:
                syllabusTracker()
            elif choice == 7:
                print("Saving your progress... ")
                time.sleep(3)
                print("\n📁 Tasks saved.\n👋 Goodbye! Stay productive.")
                break
            else:
                print("Kindly enter a valid number.")

        except Exception as e:
            print(f"Sorry! Some error occurred. \nError: {e}")
            
if __name__ == '__main__':
    main()