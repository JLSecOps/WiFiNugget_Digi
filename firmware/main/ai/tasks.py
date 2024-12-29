# Task definitions and XP mapping
def define_tasks():
    tasks = {
        "scan_networks": 5,
        "deauth_attack": 10,
        "capture_handshake": 15,
    }
    return tasks

# Example task handler
def complete_task(task_name, xp_manager):
    tasks = define_tasks()
    if task_name in tasks:
        xp_manager.add_xp(tasks[task_name])
        print(f"Task {task_name} completed! Earned {tasks[task_name]} XP.")
    else:
        print(f"Unknown task: {task_name}")
