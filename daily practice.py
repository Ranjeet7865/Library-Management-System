# Ek Python function likho jo ek list le aur usmein se sirf even numbers ko return kare.

numbers=[1,2,3,4,5,6]
even_number=[] # even number lene k liye
for num in numbers:
    if num % 2 == 0:
     even_number.append(num) #  ek list mein collect karna chahte hain, toh append ka use
print (even_number)
     # vowels count
string= input("enter the string: ").lower()
vowels = ("aeiou")
count=0
for char in string:
   if char in vowels:
     count +=1
print(f"number of vowels {count}")
# prame no. check krna 
num=int(input("enter the no.: "))
if num <=1:  # prime no. 1 se nahi 2se start hota hai
   print("not prime no.")
else:
   for i in range (2,num):
      if num % i ==0:  # Agar koi number divide kar raha hai, toh num prime nahi hai
         print("not prime no.")
         break      # Agar number divisible mil gaya toh loop ko break kar do
   else:
      print("prime no.")
      # Question: Ek Python function likho jo ek number ko input le aur uske factors print kare.
   factor = int(input("enter the number: ")) 
   for j in range (1,factor+1): # factor +1 islyi likha ki koi limit nh like hr ik input k liye ho. range mein sirf ik input k liye hona tha
       if factor % j ==0:
         print(j)
          
# Question: Ek Python function likho jo ek integer number ko input mein le aur uske liye 
# multiplication table (1 se 10 tak) print kare.
   number= int(input("enter the no. "))
   for i in range (1,11):
    print(number, "x",i, "=", number*i)
#Question: Ek Python function likho jo ek list of numbers le aur un 
#numbers ko ascending order mein sort karke return kare.
number=[12,5,3,9,1]
number.sort() #- assesnding order & desceding order- number.sort(reverse=true)
print(number)

#question: Ek Python function likho jo ek string le aur usmein har character ki frequency count kare.

frequency_string={} # Empty dictionary to store frequencie
string=input("enter the string:")
for char in string:  # Loop through each character in the string
   if char in frequency_string:
      frequency_string[char]+=1  # Increment frequency if character already exists 
      #Agar character already dictionary mein hai, toh uska count badha dete hain.
   else:
      frequency_string[char]=1   # Initialize frequency for new character 
      #Agar character pehli baar aa raha hai, toh uska count 1 set karte hain.
      #frequency print karna
for key,value in frequency_string.items(): #key mein character hoga (like 'h'),
         # aur value mein uski frequency (like 1).
         print(f"{key}: {value}")
#question:Ek Python function likho jo ek integer list le aur 
# duplicate elements ko remove karke sorted unique list return kare. remove syntax-set()
number=[3,2,1,5,4,4,3,5,6,2]
unique_list=list(set(number))  # Remove duplicates and convert back to a list
unique_list.sort() # Explicitly sort the list
print(unique_list)

#question:Ek Python program likho jo 1 se 10 tak ke numbers ko print kare using a while loop.
i=1 # start variable
while i<=10: #loop condition - i 10 tochotta ya baraber nhh h jwe
   print(i)  # print current number
   i+=1  # increment the variable
   
# Ek Python program likho jo user se ek number le aur us number ke factorial ko calculate kare using a while loop.

n = int(input("Enter a number: "))  # User input
product = 1  # Initialize product to 1
i = 1  # Start loop counter with 1

while i <= n:  # Loop runs until i reaches n
    product *= i  # Multiply product by i
    i += 1  # Increment i by 1

print(f"Factorial of {n} is {product}")  








      

   



