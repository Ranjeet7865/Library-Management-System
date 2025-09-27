"""LIBRARY MANAGEMENT
Books_avl=["rich dad poor dad","java", "powerbi", "html","thinking mind", "motivational"]
def Borrow_book ():
        book = input("enter a book name: ")
        if book in Books_avl:
          Books_avl.remove(book)
          print (f"you have borrowed'{book}'. enjoy reading!")
        else:
          print("sorry! book is not available")
def return_book():
   book = input("enter a book name: ")
   if book in Books_avl:
      print(f"{book} is already in the library")
   else:
     Books_avl.append(book)
     print(f"{book} has been returned successfully")
while True: 
    try:
      option =int(input ("choose an option:\n1.Borrow\n2.Return \n3.Available \n4.exit \n enter your option: "))
      if option == 1:
        Borrow_book()
      elif option == 2:
        return_book()
      elif option == 3:
        print ("Books available in library")
        for book in Books_avl:
           print("📘", book)
      elif option == 4:
        print ("Exit! Thanku You")
      else:
        print("Invalid choice! Please enter a number between 1 to 4.")
    except ValueError:
      print ("Invalid number! Please enter a valid number")"""
"""TO DO LIST
task_list=[]

def add_task():
        task= input("enter the task: ")
        task_list.append(task)
def view_task():
     if not task_list:
          print("no task found")
     else:    
        for i,task in enumerate(task_list,start=1):  # enumerate - use start numbering syntax
          print (f"{i}. {task}")
def remove_task():
    task= input("enter the task you want to remove: ")
    if task in task_list :
        task_list.remove(task)
        print("task removed successfully")
    else:
        print("task not found in the list.")
    
while True:
  try:
    option =int(input ("choose an option:\n1.add task\n2.view task \n3.remove task \n4.exit \n enter your option: "))
    if option == 1:
        add_task()
    elif option == 2:
        view_task()
    elif option == 3:
        remove_task()
    elif option ==4:
        print ("Exit! Thanku")
    else:
        print(" Invalid Choice!Please enter the number between 1 to 4")
  except Value Error:
    print("Invalid choice! please enter the valid number")"""
#Grocery store mini project
"""items={"Apple":30,"Banana":80,"Milk":50,"Papaya":70,"Watermelon":30}
def show_item():
    for item, price in items.items():# ithe for loop use honi bcs sari itms 
      #show karni agr ik shw krni fr if use hoga & item de agge price vi auga
        print(f"{item}-{price}") 
def buy_item(name,qty):
   if name in items:
        price= items[name]
        qty=int(qty)
        Total= price * qty
        print(f"Total for {qty} {name}(s):{Total}")
   else:
        print("item not available")
def availability_check(check): # jb user se koi value lete hai. woh value 
  #function ko deni hoti hai taaki function usi specific input ke saath kaam kare.
   if check in items:
      print(f"{check} is avaialble at price {items[check]}")
   else:
      print(f"{check} item is not avaialble")
item_name = input("Enter the item you want to check: ")
availability_check(item_name)
while True:
  try:
   print("="*30)
   option =int(input("choose an option:\n1.Show Item\n2.Buy Item\n3.Availablity Check\n4.Exit\n\nEnter your option:"))
   
   if option == 1:
       print ("="*30)
       show_item()
       
   elif option == 2:
    name=input("Enter the item what you want to buy:").title()
    qty= input("Enter the item qty you want to buy: ")
    print ("="*20)
    buy_item(name,qty)
   elif option == 3:
      check= input("enter the item check:").title()
      print("="*20)
      availability_check(check)
   elif option == 4:
       print("="*20)
       print ("Exit! Thanku")
       break
   else:
        print(" Invalid Choice!Please enter the number between 1 to 4")
  except ValueError:
   print("Invalid choice! please enter the valid number")"""
# Daily Task Planner App

def add_task():
        name=input("Enter the task name: ")
        time=input("enter the time: ")
        hour=input("enter the hours: ")
        while True:
         status=input("enter the status complete/incomplete:").lower()
         if status in["complete", "incomplete"]:
          break
         else:
          print ("invalid status! plz enter complete/incomplete")
                
        Daily_task.append({
                "name":name,
                "time":time,
                "hour":hour,
                "status":status
                })
def view_task():
    if not Daily_task:
        print ("task not found")
    else:
        for i, task in enumerate(Daily_task,start=1):
         print(f"{i}.{task}")
def task_choose():
   choose= int(input("please choose the task number: "))
   Daily_task[choose -1]["status"] ="complete" # index 0 se strt hota but humne -1 liya kyuki humne numbering 
   #start kari hai 1 se islye choose-1 kiya 0 se start ho choose-1 index hai or -1 karna index mein se like 1-1=0,2-1=1
   Daily_task[choose -1]["status"] ="incomplete"
def delete_task():
 task_name= input("please select the task name what you want to remove in the daily task list: ")
 for task in Daily_task:
    if task["name"].lower==task_name.lower():
     Daily_task.remove(task)
    print("task remove successfully")
    break
 else:
    print("task not found")

Daily_task= [
    {"name": "Python Study","time":"7 AM","hour":"2 hr","status": "incomplete"},
    {"name": "numpy","time":"8 AM","hour":"1 hr","status": "incomplete"},
    {"name": "go to office","time":"9 AM","hour":"5 hr","status": "complete"},
    {"name":"english story", "time":"5AM", "hour":"1 hr","status": "complete"},
    {"name":"SQL", "time":"6AM", "hour":"1 hr","status": "incomplete"},
    {"name":"ML", "time":"8 PM", "hour":"1 hr","status": "incomplete"}  
]

for i,task in enumerate(Daily_task,start=1):  # enumerate - use start numbering syntax
          print (f"{i}. {task['name']} - Time: {task['time']} - Hour: {task['hour']} - Status: {task['status']}")
while True:
 option =int(input("choose an option:\n1.add task\n2.view task\n3.task choose\n4.delete task\n5.Exit\n\nEnter your option:"))
 if option == 1:
    add_task()
 elif option == 2:
    view_task()
 elif option ==3:
    task_choose()
 elif option ==4:
    delete_task()

           

   
   



    
    


      