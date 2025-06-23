# 📚 Study Assistant

A simple yet effective command-line Study Assistant tool built with Python to help students manage their academic tasks, syllabus progress, and productivity rewards!

---

## 🌟 Features

- 📝 **User Signup**: Register your name and class once; your data is saved for future use.
- 📂 **Subject Manager**: Add all your subjects and track syllabus chapter-wise.
- 📋 **Task Management**:
  - Add tasks with automatic due dates.
  - View pending and completed tasks.
  - Automatically removes completed tasks older than 3 days.
- ✅ **Mark Tasks as Done**: Finish tasks and earn random coin rewards (5–50 coins).
- ⛷️ **Skip Tasks**: Don't want to do a task? Skip it using 10 coins.
- 📊 **Progress Overview**: View task and syllabus progress in clear stats.
- 💰 **Gamified Experience**: Motivates with coin rewards and progress tracking.

---

## 📁 Project Structure

```

.
├── Subjects/                # Folder containing subject files (chapters info)
├── User Info.txt            # Stores user's name, class, and signup date
├── Coins.txt                # Stores user's current coin balance
├── Tasks.txt                # Stores all user tasks
├── main.py                  # Main application file
└── README.md                # Project documentation

````

---

## ⚙️ How to Run

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/study-assistant.git
   cd study-assistant

2. **Run the Python script**

   ```bash
   python study_assistant.py
   ```

---

## 🖼 Sample CLI Interface

```
📚 Welcome to Study Assistant
Loading saved data...
📂 Tasks and syllabus loaded.
🪙 You currently have 20 coins.

============ Main Menu ============
1. ➕ Add Task
2. 📋 View Tasks
3. ✅ Mark Task as Done
4. 📊 Show Task Progress
5. ⛷️ Skip a Task
6. 📘 Syllabus Tracker
7. 💾 Save & Exit
===================================
```

---

## 🧠 Tech Stack

* Python 3.x
* `datetime`, `os`, `random`, `time`

---

## 💡 Future Ideas

* GUI version with Tkinter or PyQt
* Save data as JSON or in a SQLite DB
* Weekly performance reports
* Reminder notifications

---

## 🙌 Acknowledgements

Made with 💻 and 📚 for learners who like to stay productive and organized!

---

## 👤 Author

**Arhaan Ahmed**
*Feel free to fork and contribute!*

```

---

Let me know if you'd like help generating a `LICENSE` file, creating a GitHub repo, or writing contribution guidelines (`CONTRIBUTING.md`).
```
