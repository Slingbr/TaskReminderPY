from datetime import datetime


class TaskManager:
    def __init__(self, name, due_date, reminder_time, description=None, priority="Low", status="Pending"):
        self.name = name
        self.due_date = due_date
        self.reminder_time = reminder_time
        self.description = description
        self.priority = priority
        self.status = status
        
    def StatusComplete(self):
        self.status = "completed"
        
    def __str__(self):
        return f"Task: {self.name}\nDue: {self.due_date}\nReminder: {self.reminder_time}\nPriority: {self.priority}\nStatus: {self.status}\nDescription: {self.description}"
    
class TaskMethods:
    
        def __init__(self):
            self.TaskList = []
            
        def AddTask(self, name, due_date, reminder_time, description, priority, status):
            NewTask = TaskManager(name,due_date,reminder_time,description,priority,status)
            self.TaskList.append(NewTask)
        
        def DeleteTask(self,name):
            for Task in self.TaskList:
                if name == Task.name:
                    self.TaskList.remove(Task)
                    break
                
        def viewTasks(self):
            if not self.TaskList:
                print("no Tasks found")
            else:
                for task in self.TaskList:
                        print(task)
                        
        def markTaskComplete(self,name):
            if not self.TaskList:
                print("task not found")
            else:
                for task in self.TaskList:
                    if task.name == name:
                        task.StatusComplete()
                        print("Task marked as complete")

                        break
        
        def GetTask(self, name):
            for task in self.TaskList:
                if name == task.name:
                    return task
                return None
            
        def SaveTaskToTxt(self):
            with open("tasks.txt", "w") as file:
                for task in self.TaskList:
                    file.write(f"Task: {task.name}\n")
                    file.write(f"Due Date: {task.due_date}\n")
                    file.write(f"Reminder Time: {task.reminder_time}\n")
                    file.write(f"Priority: {task.priority}\n")
                    file.write(f"Status: {task.status}\n")
                    file.write(f"Description: {task.description}\n")
                    file.write("-----\n") 
            
        def load_tasks_from_txt(self, filename="tasks.txt"):
            try:
                with open(filename, "r") as file:
                    lines = file.readlines()

                current_task = {}
                for line in lines:
                    line = line.strip()

                    if not line:
                        continue

                    if line == "-----":
                        new_task = TaskManager(
                            name=current_task.get("Task"),
                            due_date=current_task.get("Due Date"),
                            reminder_time=current_task.get("Reminder Time"),
                            priority=current_task.get("Priority"),
                            status=current_task.get("Status"),
                            description=current_task.get("Description")
                        )
                        self.TaskList.append(new_task)
                        current_task = {}

                    else:
                        key, value = line.split(":", 1)
                        current_task[key.strip()] = value.strip()

                print("Tasks successfully loaded from file!")

            except FileNotFoundError:
                print(f"{filename} not found.")
            except Exception as e:
                print(f"Error loading tasks: {e}")
