# take three number and get average by diving 3

# and print the value using string formatin

# num1 = input("enter the first numer")
# num2 = input("enter the second number")
# num3 = input("enter the third number")

# (int(num1) + int(num2) + int(num3)) /3

num1, num2, num3 = input("enter three number comma seprated :").split(",")

print(f"your average number is {(int(num1) + int(num2) + int(num3)) /3}")