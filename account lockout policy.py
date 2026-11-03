correct_password = "admin123"
attempt = 0
while attempt < 3:
    password = input("Enter password: ")
    if  password == correct_password:
        print ("access granted - WELCOME")
        break
    else:
        print ("wrong password")
        attempt = attempt + 1
        print (f"{3 - attempt} tries left")
if attempt == 3:
    print ("Account locked - too many attempts")