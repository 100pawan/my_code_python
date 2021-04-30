
# user input

name = input("enter your name :")

# temp variable for store the user input. it's a empty variable

temp = ""

# for loop
for i in range(len(name)):

    if name[i] not in temp:

        print(f"{name[i]} : {name.count(name[i])}")

        temp += name[i]