import random
import string
length = int(input("Enter password length: "))
password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
print("Generated Password:", password)