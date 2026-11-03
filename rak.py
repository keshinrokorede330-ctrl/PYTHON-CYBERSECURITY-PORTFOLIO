username = input("enter username")
password = input("enter password")
if len(password) < 8:
    print ("password too short")
else:
    print("length is ok")
has_number = False
for char in password:
    if char.isdigit():
        has_number = True
if len(password) >= 8 and has_number:
    print(f"Access granted for {username}")
else:
    print(f"Access denied - weak password, try again {username}")
