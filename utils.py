from datetime import datetime

def get_status_emoji(status):
    """Return appropriate emoji for task status"""
    return "✅" if status == 'completed' else "🕒"

def get_priority_emoji(priority):
    """Return appropriate emoji for task priority"""
    emoji_map = {
        'high': '🔴',
        'medium': '🟡',
        'low': '🟢'
    }
    return emoji_map.get(priority, '⚪')

def format_task_display(task):
    """Format a task for display"""
    status_emoji = get_status_emoji(task['status'])
    priority_emoji = get_priority_emoji(task['priority'])
    
    task_str = (
        f"\n🆔 ID: {task['id']}\n"
        f"📌 Name: {task['name']}\n"
        f"📝 Description: {task['description']}\n"
        f"{priority_emoji} Priority: {task['priority'].capitalize()}\n"
        f"{status_emoji} Status: {task['status'].capitalize()}\n"
        f"📅 Due Date: {task['due_date'] or 'Not set'}\n"
        f"🕒 Created: {task['created_at']}\n"
    )
    
    if task['status'] == 'completed':
        task_str += f"🎉 Completed: {task['completed_at']}\n"
    
    task_str += "-"*40
    return task_str

def display_task_list(tasks):
    """Display a list of tasks"""
    print("\n" + "="*50)
    print("🌟 Gamma Task List 🌟".center(50))
    print("="*50)
    
    if isinstance(tasks, str):
        print(tasks)
        return
    
    for task in tasks:
        print(format_task_display(task))