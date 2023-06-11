import random

print("Welcome to my password generator.\n")

nlet = int(input("How many letters would you like in your password ?\n"))

nnumb = int(input("How many numbers would you like in your password ?\n"))

nsymb = int(input("How many symbols would you like in your password ?\n"))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@']

password_list = []

for char in range(1, nlet + 1):
  password_list.append(random.SystemRandom().choice(letters))

for char in range(1, nsymb + 1):
  password_list.append(random.SystemRandom().choice(symbols))

for char in range(1, nsymb + 1):
  password_list.append(random.SystemRandom().choice(numbers))

random.SystemRandom().shuffle(password_list)

password = ""

for char in password_list:
  password += char

print(f"Your password is: {password}")
