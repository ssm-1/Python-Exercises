#Check Palindrome Number

num = (input(print("enter a number : ")))


if num[::-1] == num[0:]:   
    print("Yes it's palindrome")
else: 
    print("No it ain't palindrome")
