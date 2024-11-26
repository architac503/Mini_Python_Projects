name = input("Type your name: ")
print("Welcome", name , "to this adventure!")

answer = input("You are on a dirt road now and it has come to an end.\nYou can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You have come to a river. You can walk around or swim accross it. (walk/swim): ").lower()
    if answer == "walk":
        print("You walked for miles and got dehydrated. You lose.")
    elif answer == "swim":
        print("You swam accross and were eaten by an alligator. You lose.")
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input("You have come to a bridge, it looks wobbly. Do you want to cross it or head back? (cross/back): ")
    if answer == "back":
        print("You go back to the dirt road. You lose.")
    elif answer == "cross":
        answer =input("You crossed the bridge and meet a stranger. Do you want to talk to them? (yes/no): ").lower()
        if answer == "yes":
            print("You talked to the stranger and they gave you the secret treasure. You win!")
        elif answer == "no":
            print("You ignored the stranger and they got offended. You lose.")
        else:
            print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.")
else:
    print("Not a valid option. You lose.")