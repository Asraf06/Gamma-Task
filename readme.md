<div align="center">
  <h1>🎯 Gamma Task Manager</h1>
  <p>
    <strong>A command-line task manager with emoji flair ✨</strong>
  </p>
  
  <p>
    <img src="https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white" alt="Python version">
    <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
    <img src="https://img.shields.io/badge/Platform-CLI-lightgrey" alt="Platform">
  </p>
</div>

<div align="center">
  <img src="https://imgur.com/iL9NltQ" width="600" alt="Gamma Task Manager Demo">
</div>

## 🚀 Features

<table>
  <tr>
    <td width="30%">
      <h3>📝 Task Management</h3>
      <ul>
        <li>Add/Edit/Delete tasks</li>
        <li>Priority levels (🟢/🟡/🔴)</li>
        <li>Due date tracking</li>
      </ul>
    </td>
    <td width="30%">
      <h3>📂 Data Handling</h3>
      <ul>
        <li>Auto-save to JSON</li>
        <li>TXT exports</li>
        <li>UTF-8 support</li>
      </ul>
    </td>
    <td width="30%">
      <h3>🎨 CLI Interface</h3>
      <ul>
        <li>Emoji-rich UI</li>
        <li>Task filtering</li>
        <li>Color-coded priorities</li>
      </ul>
    </td>
  </tr>
</table>

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/gamma-task-manager.git

# Navigate to project
cd gamma-task-manager

# Run the application
python -m gamma_task.main
```

## 🖥️ Usage Demo

```plaintext
🎯 Gamma Task Manager 🎯
==============================
1. ➕ Add Task
2. 📋 List All Tasks
3. ✔️ Complete Task
4. ✏️ Edit Task
5. 🗑️ Delete Task
6. 📤 Export Tasks
7. 🚪 Exit

🔹 Choose an option: 2
```

## 📂 Project Structure

```bash
gamma_task/
├── __init__.py
├── main.py          # CLI interface
├── task_manager.py  # Core logic
└── utils.py         # Display helpers
data/                # Auto-created storage
exports/             # Export directory
```

## 🌟 Example Workflow

<details>
<summary>📝 Adding a Task</summary>

```plaintext
📝 Enter task name: Finish Project
📄 Enter description: Complete docs
📅 Enter due date (YYYY-MM-DD): 2023-12-31
🔝 Enter priority (high/medium/low): high

✅ Task 'Finish Project' added!
```
</details>

<details>
<summary>📤 Exporting Tasks</summary>

```plaintext
📄 Enter export filename [gamma_export.txt]: 
📤 Exported to 'exports/gamma_export.txt'!
```
</details>

## 🤝 Contributing

```bash
1. Fork the project
2. Create your feature branch (git checkout -b feature/AmazingFeature)
3. Commit your changes (git commit -m 'Add some amazing feature')
4. Push to the branch (git push origin feature/AmazingFeature)
5. Open a Pull Request
```

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---

<div align="center">
  Made with ❤️ and Python 🐍
</div>
```