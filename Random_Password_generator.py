#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '<', '>', '?', '/', '@', '{', '}']

print("Create a Random Strong Password Generator using Python!")
all_letters = int(input("How many letters would you like in your password: ")) 
special_symbols = int(input(f"How many special symbols would you like: "))
all_numbers = int(input(f"How many numbers would you like: "))

#Eazy Level
password = ""
for char in range(1, all_letters + 1):
    password += random.choice(letters)
    
for char in range(1, special_symbols + 1):
    password += random.choice(symbols)
    
for char in range(1, all_numbers + 1):
    password += random.choice(numbers)
    
print(f"The Eazy Level Password is: {password} \n") 
   


#Hard Level

password_list = []
for char in range(1, all_letters + 1):
    password_list += random.choice(letters)
    
for char in range(1, special_symbols + 1):
    password_list += random.choice(symbols)
    
for char in range(1, all_numbers + 1):
    password_list += random.choice(numbers)
random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"The Hard Level Password is: {password}")

