# if_elif_else


# age = 0 to 4 (ticket : free)

# age = 5 t0 10 (ticket : 150)

# age = 11 to  15 (ticket : 200)

# age = above 20 (ticket : 500)


age = int(input("Enter your age :"))

if age >= 0 or age == 0 and age == 4:
    print("Ticket is free")

elif age >= 5 and age == 10:
    print("ticket price : 150")

elif age >= 11 and age ==  15:
    print("ticket price : 200")   

elif age >= 20 :
    print("ticket price : 500")    
else:
    print("not allowed")