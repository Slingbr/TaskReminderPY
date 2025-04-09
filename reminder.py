import time
from datetime import datetime
from task_manager import TaskMethods

class ReminderService:
    def __init__(self, task_methods):
        self.task_methods = task_methods

    def check_reminders(self):
        
        current_time = datetime.now().strftime("%H:%M")
        for task in self.task_methods.TaskList:
            if task.reminder_time == current_time and task.status != "completed":
                print(f"Reminder: Task '{task.name}' is due now!")

    def start_reminder_check(self):
        print("Reminder service started.")
        while True:
            self.check_reminders()
            time.sleep(60)