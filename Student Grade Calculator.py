# student grade calculator- dict, variables,loops,if else,function
# Empty dictionary to store students' data
students_data={}
# Input loop to collect student data
num_student = int(input("Enter number of students: "))

# Function to calculate average score
def CalculateAverage(scores):
    return sum(scores)/ len(scores)
# Function to determine grade        
def getGrade(average):
    if average >= 98:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return'c'
    elif average >=60:
        return 'd'
    else:
        return 'f'
    
for _ in range (num_student): # '_ 'matlab hai ki loop variable ka use nahi ho raha
    name=input("Enter Student Name: ")
    scores= []
    for subject in ('Math', 'English','Science','Hindi'):
        score = int(input(f"enter {name}'s is {subject}:"))
        scores.append(score)
    students_data [name]=scores

for name,scores in students_data.items():
# Display each student's average and grade
    average = CalculateAverage(scores)
    grade = getGrade(average)
    print(f"{name}'s Average Score: {average:.2f}") # .2 ka matlab hai ki decimal ke baad sirf 2 digits show honi chahiye.
    print(f"{name}'s Grade: {grade}")

    # Library Management System

    library = {
        "To Kill a Mokingword": "Harper Lee",
        "1984": "George Orwell",
        "Pride and Prejudice": "Jane Austan",
        "The Great Getsby": "f. Scott Fitzgerald",
        "The Catcher in the Rye": "J.D Salinger"
    }
    def add_book():
        book_name = input("Enter the book name: ")
        author_name=input("Enter the author name: ")
        library[book_name] = author_name
        print (f"'{book_name}' by {author_name}")

    def search_book():
        book_name = input ("Search the book name: ")
        if book_name in library:
            print (f"'{book_name}'is written by {library[book_name]}") # dict mein specific key ko acess karne k liye[]
        else:
            print (f"'{book_name}' book is not found")
    def del_book():
        book_name = input ("delete the book name: ")
        if book_name in library:
           del library[book_name]
           print(f"'{book_name}'has been deleted from the libraray")
        else:
         print(f"'{book_name}'not found in libraray")
    def display_books():  
        if library:
            print("books avilable in the library")  
            for book,author in library.items():  # library items likhte hai ye har key (book name or author) ko pair ch lai anda
                print(f"'{book}' by {author}")
        else:
            print("the libarary is empty")
    while True:
      choice = int(input("enter the choice: \n1.add_book\n2.search book\n3. del_book\n4. dislay book\n5.exit\n"))
      if choice == 1:
          add_book()
      elif choice ==2:
            search_book()
      elif choice == 3:
            del_book()
      elif choice ==4:
            display_books ()
      elif choice ==5:
            print("exit the program")
            break # exit loop
      else:
            print("invalid choice")

# number divisible hai ya nahi 5 aur 3 dono se.

number= int(input("enter the no.:= "))
if number % 5==0 and number % 3 ==0:
    print("divisible by both")
elif number % 3 == 0:
    print("dividible by 3 only")
elif number % 5 == 0:
    print("divisible by 5 only")
else:
    print("not divisible by 5 or 3")







