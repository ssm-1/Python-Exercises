#Merge two lists using the following condition: ODd from first even from second

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
list3 = []

for i in range(len(list1)): 
    if list1[i] % 2 == 1: 
        list3.append(list1[i])
    if list2[i] % 2 == 0: 
        list3.append(list2[i])

print(list3)
