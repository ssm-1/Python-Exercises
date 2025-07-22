#Exercise 21: Check if a user-entered string contains any digits using a for loop
string = input("Enter an alphanumeric string ")

count = 0

for i in range(len(string)): 
    if string[i].isdigit(): 
        count += 1
    
print(f"The string has {count} digits")
        


