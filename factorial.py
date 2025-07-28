print("FACTORIAL OF A GIVEN NUMBER \n")

num = int(input("Enter number: ")) 

final = 1
temp = 1
temp1 = 1
temp2 = 1

for i in range(num, 0, -1): 
    final *= i

print(f"factorial is {final}")    
