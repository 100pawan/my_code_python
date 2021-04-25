# user input comma seprated

name, char = input("Enter your name & first word of your name  ").split(",") #comma seprated 

print(f"you entered {len(name)} \nyour character {name.lower().count(char.lower())}")

# name.lower().count(char.lower())

# char.lower()