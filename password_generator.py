#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
length= int(input("What is the length of the password that you would like?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#generating the password sequence
password_list=[]
for symbol in range(0,nr_symbols):
  password_list+=random.choice(symbols)
for number in range(0,nr_numbers):
  password_list+=random.choice(numbers)
for letter in range(0,(length-(nr_symbols+nr_numbers))):
  password_list+=random.choice(letters)

#shuffling the list, to generate a completely random password
random.shuffle(password_list)

#converting list to string
password=''.join([str(char) for char in password_list])

#printing the generated password
print("A password choice could be: " + password)