import random

winning_nummber =random.randint(1, 100)

user = int(input("enter the number :"))

chance = 1

game_over = False

while not game_over :
    if user == winning_nummber:
        print(f"you win this is your correct guess {chance} in time\n")

        game_over = True

    else:
        if user > winning_nummber:
            print("ohh so high ! guess again--->\n")
            chance += 1
            user = int(input("enter the number agin :\n"))
        else:
            print("you guess too low !!!!!!!!!")

            chance += 1
            user = int(input("enter the number again :\n"))
        
    