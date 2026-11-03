import random
import string
length = int(input("HOW LONG SHOULD PASSWORD BE? "))
letters_and_numbers = string.ascii_uppercase+ string.digits + string.punctuation
password = ""
for i in range(length):
    password = password + random.choice(letters_and_numbers)
print (f"GENERATED PASSWORD : {password}")