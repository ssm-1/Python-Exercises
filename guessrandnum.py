import random
real = random.randint(1, 9)
temp = int(input("ENTER A NUMBER: "))

while temp != real: 
    temp = int(input("Guess the damn number: \n"))

else: 
    print("Congrats you guessed it! ")