# sum of the number like 1 + 2+ 3  = 6
# 1. user input 
# 2. store the value in any variable 

# i am doing indexing so i dont use int(input)----------->

num = input("enter the number :")

total = 0

for i in range(0, len(num)):

    total += int(num[i])

print(total)    