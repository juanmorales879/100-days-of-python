import random,string


password = []
user_letter = int(input("How many letters would you like in your password: "))
user_symbols = int(input("How many symbols would you like in your password: "))
user_numbers = int(input("How many numbers would you like in your password: "))
total = user_letter + user_numbers + user_symbols

for _ in range(total):
    if user_letter > 0:
        password.append(random.choice(string.ascii_letters))
        user_letter-=1
    if user_numbers > 0:
        password.append(random.choice(string.digits))
        user_numbers-=1
    if user_symbols > 0:
        password.append(random.choice(string.punctuation))
        user_symbols-=1       

print(f"Your password is {''.join(password)}")  
    
