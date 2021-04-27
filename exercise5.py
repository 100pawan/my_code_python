
name = input("enter your name : ")

age = int(input("enter your age :"))

age += 18

print(f"your name is {name.center(len(name) +8, '*')} and your age is {str(age)}")