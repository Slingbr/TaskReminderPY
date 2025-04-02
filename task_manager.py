from datetime import datetime


class TaskManager:
    def __init__(self, name, due_date, reminder_time, description=None, priority="Low", status="Pending"):
        self.name = name
        self.due_date = due_date
        self.reminder_time = reminder_time
        self.description = description
        self.priority = priority  # Priority: Low, Medium, High
        self.status = status  # Status: Pending, Completed
        
    def StatusComplete(self):
        self.status = "completed"
    
    class TaskMethods:
        def __init__(self):
            TaskList = []
            
        def AddTask(self, name, due_date, reminder_time, description, priority, status):
            NewTask = TaskManager(name,due_date,reminder_time,description,priority,status)
            self.TaskList = TaskList.Append(NewTask)
        
        