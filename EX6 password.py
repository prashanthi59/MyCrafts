name = input("Type your name: ")
print("Welcome", name, "to this advencture!")

answer = input("You are on adirt road, it has come to an end and you can go left or right,which way to you go: ").lower()
if answer=="left":
    answer = input("You come to a river, you can walkaround it or swim accross? Type  walk to walk around and swim to swim accross: ")

    if answer =="swim":
        print(" You swim accross and were  eaten by an alligator.")
    elif answer == "walk":
        print(" You walked for many miles, ran out of water and you lost the game.")
    else:
        print('not a valid option. You lose.')
elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you want to accross  it or head back(cross/back)? ")

    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input("You cros to a bridge, and meet a stranger.Do you talk them (Yes/No)? ")
        if answer == "yes":
            print("You talk the stranger and they are offenf=ds and you WIN!")
        elif answer == "no":
            print("Not a valid option .you lost.")
        else:
            print("Not a valid answer ")
    else:
        print('not a valid option. You lose.')
