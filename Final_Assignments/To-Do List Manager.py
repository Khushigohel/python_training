''' Create a Python script that implements a simple to-do list manager.
● Allow users to add tasks, mark tasks as completed, and remove tasks.
● Store the tasks in a list of dictionaries where each dictionary represents a task with keys 
like 'task_name', 'priority', 'completed', etc.
● Provide a menu-driven interface for users to interact with the to-do list.
'''
class Task:
    def __init__(self,name,priority):
        self.name=name
        self.priority=priority
        self.completed=False
        
    def mark_completed(self):
        self.completed = True
        
class ToDoList:
    def __init__(self):
        self.tasks=[]
    
    def add_task(self):
        name=input("Enter the  Task Allocation Name:")
        priority=input("Enter the Task Priority (Low,Medium,High) :")
        
        task=Task(name,priority)
        self.tasks.append(task)
        print("\n Task Sucessfully Add... ")
    
    def Display_Task(self):
        if not self.tasks:
            print("No Task Avaliable")
        
        print("Current Tasks")
        print("-"*50)
        
        for index,task in enumerate(self.tasks,start=1):
            status = "Completed" if task.completed  else "Pandding"
            print(f"{index} | Task Name: {task.name} | Priority: {task.priority} | Status: {status}")
        print("-"*50)
    
    def mark_number(self):
        self.Display_Task()
        if not self.tasks:
            print("No Task Avaliable")
        try:
            task_no=int(input("Enter task number to mark completed: "))
            self.tasks[task_no -1 ].mark_completed()
            print("\nTask marked as completed!\n")
        except:
            print("\nInvalid task selection!\n")
    def remve_task(self):
        self.Display_Task()
        if not self.tasks:
            print("No Task Avaliable")
        try:
             task_no=int(input("Enter task number to mark completed: "))
             self.tasks.pop(task_no -1)
             print("\n task Remove Sucessfulll...")
        except:
            print("\nInvalid task selection!\n")
    
    def menu(self):
        while True:
            print("Welcome To-Do List manager...")
            print("\n 1. Add the Task")
            print("\n 2. Dispaly the Task")
            print("\n 3. Mark As completed")
            print("\n 4. Remove Task")
            print("\n 5.Exit")
            
            choice=int(input("Enter the Choice:"))
            if choice == 1:
                self.add_task()
            elif choice ==2:
                self.Display_Task()
            elif choice ==3:
                self.mark_number()
            elif choice ==4:
                self.remve_task()
            else:  
                exit()

obj=ToDoList()
obj.menu()

      