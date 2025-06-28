from task_manager import GammaTask
from utils import display_task_list

def display_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print("🎯 Gamma Task Manager 🎯".center(50))
    print("="*50)
    print("1. ➕ Add Task")
    print("2. 📋 List All Tasks")
    print("3. ✔️ Complete Task")
    print("4. ✏️ Edit Task")
    print("5. 🗑️ Delete Task")
    print("6. 📤 Export Tasks to TXT")
    print("7. 🚪 Exit")

def get_task_input():
    """Get task details from user"""
    name = input("📝 Enter task name: ")
    desc = input("📄 Enter task description (optional): ")
    due_date = input("📅 Enter due date (YYYY-MM-DD, optional): ")
    priority = input("🔝 Enter priority (high/medium/low, default medium): ").lower() or "medium"
    return name, desc, due_date if due_date else None, priority

def main():
    task_manager = GammaTask()
    
    while True:
        display_menu()
        choice = input("\n🔹 Enter your choice (1-7): ")
        
        if choice == "1":
            name, desc, due_date, priority = get_task_input()
            print(task_manager.add_task(name, desc, due_date, priority))
            
        elif choice == "2":
            print("\n🔍 Filter options:")
            print("1. All tasks")
            print("2. Pending tasks")
            print("3. Completed tasks")
            print("4. Filter by priority")
            filter_choice = input("🔹 Enter filter choice (1-4): ")
            
            if filter_choice == "1":
                tasks = task_manager.list_tasks()
            elif filter_choice == "2":
                tasks = task_manager.list_tasks(filter_status="pending")
            elif filter_choice == "3":
                tasks = task_manager.list_tasks(filter_status="completed")
            elif filter_choice == "4":
                priority = input("🔝 Enter priority to filter (high/medium/low): ").lower()
                tasks = task_manager.list_tasks(filter_priority=priority)
            else:
                print("⚠️ Invalid filter choice!")
                continue
                
            display_task_list(tasks)
                
        elif choice == "3":
            task_id = input("🔢 Enter task ID to mark as complete: ")
            try:
                print(task_manager.complete_task(int(task_id)))
            except ValueError:
                print("⚠️ Please enter a valid task ID (number)!")
                
        elif choice == "4":
            task_id = input("🔢 Enter task ID to edit: ")
            try:
                task_id = int(task_id)
                print("\n✏️ Leave field blank to keep current value")
                name = input(f"📝 New name: ")
                desc = input(f"📄 New description: ")
                due_date = input(f"📅 New due date (YYYY-MM-DD): ")
                priority = input(f"🔝 New priority (high/medium/low): ").lower()
                status = input(f"🔄 New status (pending/completed): ").lower()
                
                updates = {}
                if name: updates['name'] = name
                if desc: updates['description'] = desc
                if due_date: updates['due_date'] = due_date
                if priority in ['high', 'medium', 'low']: updates['priority'] = priority
                if status in ['pending', 'completed']: updates['status'] = status
                
                if updates:
                    print(task_manager.edit_task(task_id, **updates))
                else:
                    print("ℹ️ No changes made.")
            except ValueError:
                print("⚠️ Please enter a valid task ID (number)!")
                
        elif choice == "5":
            task_id = input("🔢 Enter task ID to delete: ")
            try:
                print(task_manager.delete_task(int(task_id)))
            except ValueError:
                print("⚠️ Please enter a valid task ID (number)!")
                
        elif choice == "6":
            filename = input("📄 Enter export filename (default: gamma_tasks_export.txt): ") or "gamma_tasks_export.txt"
            print(task_manager.export_to_txt(filename))
            
        elif choice == "7":
            print("\n👋 Thank you for using Gamma Task Manager! Goodbye!")
            break
            
        else:
            print("⚠️ Invalid choice! Please enter a number between 1-7.")

if __name__ == "__main__":
    main()