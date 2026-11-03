num = 0
num = int(input("enter number: "))
if num >= 5 and num <=30:
    decimalcode = num + 60
    letter = chr(decimalcode)
    print(str(num) + " is equal to " + letter)
else:
    print("invalid input")