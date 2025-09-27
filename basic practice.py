"""def is_armstrong(num):
    digits = str(num)  
    power = len(digits)  
    total = sum(int(digit) ** power for digit in digits)  
#
    return total == num  

# Taking input
number = int(input("Enter a number: "))

# Checking Armstrong Number
if is_armstrong(number):
    print(f"{number} is an Armstrong Number!")
else:
    print(f"{number} is NOT an Armstrong Number.")"""
"""def number(num1,num2):
    sum(num1+num2)
    number = int(input("Enter a number: "))

    return(sum)"""

"""def check_even_odd(num):
    if num % 2 ==0:
        return "even"
    else:
     return "odd"
number= int(input("Enter a number: "))
result = check_even_odd
print(result)"""
# ATM PROGRAM
def check_pin():
    correct_pin=1234
    attempt = 0
    while attempt <= 3:
        user_pin=int(input("enter the pin: "))
        if user_pin == correct_pin:
            print("pin correct! welcome to your account:")
            return True  # PIN सही है, तो आगे बढ़ो
        else:
            attempt += 1
            print(f"❌ Incorrect PIN! {3 - attempt} attempt left.")

    print("🚫 Too many incorrect attempts. Exiting...")
    return False  # 3 बार गलत PIN डालने पर exit

# Step 2: पहले सिर्फ PIN check करो
if check_pin():
    print("✅ Now, show menu options...")
    balance = 5000
while True:
    try:
      option =int(input ("choose an option:\n1.check balance\n2.withdraw \n3.deposit \n4.exit \n enter your option: "))
      if option in [1,2,3,4]:
       break
      else:
       print ("invalid choice ! please enter a number b/w 1 to 4")
    except:
     print ("invalid input!please enter a valid number:")



     
    


         


        
        

    

    
 

