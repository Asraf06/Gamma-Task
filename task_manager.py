import json
import os
from datetime import datetime
from pathlib import Path

class GammaTask:
    def __init__(self):
        self.tasks = []
        self.data_file = 'gamma_tasks.json'
        self.ensure_data_directory()
        self.load_tasks()
    
    def ensure_data_directory(self):
        """Ensure the data directory exists"""
        Path('data').mkdir(exist_ok=True)
        Path('exports').mkdir(exist_ok=True)
        
    def load_tasks(self):
        """📂 Load tasks from JSON file"""
        try:
            if os.path.exists(f'data/{self.data_file}'):
                with open(f'data/{self.data_file}', 'r') as f:
                    self.tasks = json.load(f)
        except Exception as e:
            print(f"⚠️ Error loading tasks: {e}")
    
    def save_tasks(self):
        """💾 Save tasks to JSON file"""
        try:
            with open(f'data/{self.data_file}', 'w') as f:
                json.dump(self.tasks, f, indent=4)
        except Exception as e:
            print(f"⚠️ Error saving tasks: {e}")
    
    def add_task(self, name, description="", due_date=None, priority="medium"):
        """➕ Add a new task"""
        task = {
            'id': len(self.tasks) + 1,
            'name': name,
            'description': description,
            'due_date': due_date,
            'priority': priority.lower(),
            'status': 'pending',
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'completed_at': None
        }
        self.tasks.append(task)
        self.save_tasks()
        return f"✅ Task '{name}' added successfully!"
    
    def list_tasks(self, filter_status=None, filter_priority=None):
        """📋 List all tasks with optional filters"""
        if not self.tasks:
            return "📭 No tasks found!"
            
        filtered_tasks = self.tasks
        
        if filter_status:
            filtered_tasks = [t for t in filtered_tasks if t['status'] == filter_status]
            
        if filter_priority:
            filtered_tasks = [t for t in filtered_tasks if t['priority'] == filter_priority.lower()]
        
        return filtered_tasks
    
    def complete_task(self, task_id):
        """✔️ Mark a task as completed"""
        for task in self.tasks:
            if task['id'] == task_id:
                task['status'] = 'completed'
                task['completed_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_tasks()
                return f"🎉 Task '{task['name']}' marked as completed!"
        return f"⚠️ Task with ID {task_id} not found!"
    
    def delete_task(self, task_id):
        """🗑️ Delete a task"""
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                deleted_name = task['name']
                del self.tasks[i]
                # Reassign IDs to maintain order
                for idx, t in enumerate(self.tasks, start=1):
                    t['id'] = idx
                self.save_tasks()
                return f"🗑️ Task '{deleted_name}' deleted successfully!"
        return f"⚠️ Task with ID {task_id} not found!"
    
    def edit_task(self, task_id, **kwargs):
        """✏️ Edit task properties"""
        for task in self.tasks:
            if task['id'] == task_id:
                valid_fields = ['name', 'description', 'due_date', 'priority', 'status']
                for key, value in kwargs.items():
                    if key in valid_fields:
                        task[key] = value
                self.save_tasks()
                return f"✏️ Task '{task['name']}' updated successfully!"
        return f"⚠️ Task with ID {task_id} not found!"
    
    def export_to_txt(self, filename="gamma_tasks_export.txt"):
        """📤 Export tasks to a text file in exports folder"""
        try:
            export_path = Path('exports') / filename
            with open(export_path, 'w', encoding='utf-8') as f:
                f.write("="*50 + "\n")
                f.write("Gamma Task Export\n".center(50))
                f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("="*50 + "\n\n")
                
                for task in self.tasks:
                    status_emoji = "✅" if task['status'] == 'completed' else "🕒"
                    priority_emoji = {
                        'high': '🔴',
                        'medium': '🟡',
                        'low': '🟢'
                    }.get(task['priority'], '⚪')
                    
                    f.write(f"🆔 ID: {task['id']}\n")
                    f.write(f"📌 Name: {task['name']}\n")
                    f.write(f"📝 Description: {task['description']}\n")
                    f.write(f"{priority_emoji} Priority: {task['priority'].capitalize()}\n")
                    f.write(f"{status_emoji} Status: {task['status'].capitalize()}\n")
                    f.write(f"📅 Due Date: {task['due_date'] or 'Not set'}\n")
                    f.write(f"🕒 Created: {task['created_at']}\n")
                    if task['status'] == 'completed':
                        f.write(f"🎉 Completed: {task['completed_at']}\n")
                    f.write("-"*40 + "\n\n")
            
            return f"📤 Tasks exported successfully to 'exports/{filename}'!"
        except Exception as e:
            return f"⚠️ Error exporting tasks: {e}"