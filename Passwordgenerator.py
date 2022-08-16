import random

print("Welcome to my password generator.\n")

nlet = int(input("How many letters would you like in your password ?\n"))

nnumb = int(input("How many numbers would you like in your password ?\n"))

nsymb = int(input("How many symbols would you like in your password ?\n"))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@']

# total = nlet + nnumb + nsymb

# password = ""
# count1 = count2 = count3 = 0

# while len(password) != total:

#     guess = random.randint(1, 3)

#     if guess == 1 and count1 != nlet:
#         password += random.choice(letters)
#         count1 += 1
#     if guess == 2 and count2 != nnumb:
#         password += random.choice(numbers)
#         count2 += 1
#     if guess == 3 and count3 != nsymb:
#         password += random.choice(symbols)
#         count3 += 1

# print(f"Your password is {password}")


password_list = []

for char in range(1, nlet + 1):
  password_list.append(random.choice(letters))

for char in range(1, nsymb + 1):
  password_list.append(random.choice(symbols))

for char in range(1, nsymb + 1):
  password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""

for char in password_list:
  password += char

print(f"Your password is: {password}")
