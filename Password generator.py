import random 

def password_generator(length):
    characters ="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890/?!@#$%&*"
    password =""
    for i in range(length):
        password = password + (random.choice(characters))
    return password
length_password = int(input("Enter the length of the password you required "))
print(password_generator(length_password))

