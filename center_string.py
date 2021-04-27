# center string method 
# its help  to add anything in your string befre and last 

# eg  pawan ------>   **pawan**


# name = "pawan"

# # print(name.center(7 +1 +1, "*"))
# print(name.center(9, "*")) # first you conut the lentgh of your string and then plus in 

# smalll program 

name = input("enter your name plz\n")

print(f"output of your name is{name.center(len(name) +8, '*')}")