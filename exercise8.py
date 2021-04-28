
number = input("enter the number :")

# lentgh check kr ke add karwana hai 
# eg 1 + 2 + 3 = 6

# using while Loop

total = 0 

i  = 0

while i < len(number):
    total += int(number[i])

    i = i +1
print(total)


