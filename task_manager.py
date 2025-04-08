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
        
    def __str__(self):
        return f"Task: {self.name}\nDue: {self.due_date}\nReminder: {self.reminder_time}\nPriority: {self.priority}\nStatus: {self.status}\nDescription: {self.description}"
    
    class TaskMethods:
        def __init__(self):
            self.TaskList = []
            
        def AddTask(self, name, due_date, reminder_time, description, priority, status):
            NewTask = TaskManager(name,due_date,reminder_time,description,priority,status)
            self.TaskList = self.TaskList.Append(NewTask)
        
        def DeleteTask(self,name):
            for Task in self.TaskList:
                if Task.name == name:
                    self.TaskList.remove(Task)
                    break
                
        def viewTasks(self,name):
            if not self.TaskList 
                print("no Tasks found")
            else:
                for task in self.TaskList:
                    if task.name == name:
                        print(task)