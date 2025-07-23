
num = int(input("Enter a number between 1 and 1000"))

while num > 1000 or num < 1: 
    print("Out of range")
    num = int(input("Enter a number between 1 and 1000"))


while num < 1000 and num != 384 and num > 1: 
    print("Whoop. Wrong number. Try again.")
    num = int(input("Enter a number between 1 and 1000"))
else: 
    print("Congrats! You made it. ! !")
