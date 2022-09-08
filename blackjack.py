import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
game_exit = False
while not game_exit:  
    user = [random.choice(cards), random.choice(cards)]
    comp = [random.choice(cards), random.choice(cards)]
    print()
    print(f"you got cards as {user}")
    print(comp)
    print(f"Comp got cards as {comp[0]}")
    ask = input("Do you want to dealt a card (yes or no):  ")
    if ask == 'yes':
        if sum(user) >= 17:
            cards.remove(11)
            cards.append(1)
            user.append(random.choice(cards))
            print(user)
            print(sum(user))
        elif sum(user) < 17:
            user.append(random.choice(cards))
            print(user)
            print(sum(user))
    else:
        print(sum(user))
    if sum(comp) < 17:
        comp.append(random.choice(cards))
    else:
        print(sum(comp))

    if (sum(user) == sum(comp)):
        print("Its a Tie")
    elif ((sum(user) and sum(comp)) > 21):
        print("Comp Won the Game")
    elif sum(user) > sum(comp) and sum(user) <= 21 or sum(comp) > 21:
        print("User won the game")
    else:
        print("Comp won the game")
    print(sum(user))
    print(sum(comp))
    want_to_play = input("Want to play again: yes or no \n")
    if want_to_play == 'yes':
        continue
    else:
        game_exit = True