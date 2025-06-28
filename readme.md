Gamma Task Manager
https://img.shields.io/badge/Python-3.8+-blue?logo=python
📌 A command-line task manager with emoji flair

Features ✨
✅ CRUD Operations

Add, list, complete, edit, and delete tasks

Priority levels (🟢 Low, 🟡 Medium, 🔴 High)

Due dates and completion tracking

📂 Data Management

Automatic JSON storage in data/ folder

Export tasks to TXT files in exports/

🎨 User-Friendly CLI

Emoji-rich interface

Filter tasks by status/priority

UTF-8 support for exports

Installation ⚙️
Clone the repository:

bash
git clone https://github.com/yourusername/gamma-task-manager.git
Navigate to the project:

bash
cd gamma-task-manager
Run the application:

bash
python -m gamma_task.main
Usage 🖥️
plaintext
🎯 Gamma Task Manager 🎯
==============================
1. ➕ Add Task
2. 📋 List All Tasks
3. ✔️ Complete Task
4. ✏️ Edit Task
5. 🗑️ Delete Task
6. 📤 Export Tasks to TXT
7. 🚪 Exit
Project Structure 📂
bash
gamma_task/
├── __init__.py
├── main.py          # CLI interface
├── task_manager.py  # Core logic
└── utils.py         # Display helpers
data/                # Auto-created for JSON storage
exports/             # Auto-created for TXT exports
Examples 💡
Adding a Task
plaintext
📝 Enter task name: Finish Project  
📄 Enter task description: Complete docs and tests  
📅 Enter due date (YYYY-MM-DD): 2023-12-31  
🔝 Enter priority (high/medium/low): high  
✅ Task 'Finish Project' added successfully!
Exporting Tasks
plaintext
📤 Tasks exported successfully to 'exports/gamma_tasks_export.txt'!
Dependencies 📦
Python 3.8+

No external libraries required

License ⚖️
MIT License - Free for personal and commercial use.

Contributing 🤝
Pull requests welcome! For major changes, open an issue first.

Happy task managing! 🎉