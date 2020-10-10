import random

class deck:
    def __init__(self,difficulty):
        self.difficulty = difficulty
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades","Hearts","Clubs","Diamonds"]:
            for v in range(2,11):
                self.cards.append((v,s))
        for f in ["Spades","Hearts","Clubs","Diamonds"]:
            for b in ["Jack","Queen","King","Ace"]:
                self.cards.append((b,f))

    def hit(self):
        card = random.choice(self.cards)
        self.cards.remove(card)
        return card

def calculatehandvalue(hand):
    value = 0
    for x in hand:
        if x[0] in ["Jack", "Queen", "King"]:
            value += 10
        elif x[0] in ["Ace"]:
            pass
        else:
            value += x[0]
    return value

def checkforace(hand,value):
    for x in hand:
        if x[0] in ["Ace"]:
            if value+11 > 21:
                value += 1
            else:
                value += 11
        else:
            pass
    return value


def checkforbj(value1,value2):
    if value1 == 21 and value2 != 21:
        print("Player BlackJack! You win!")
        return 1
    elif value2 == 21 and value1 != 21:
        print("Dealer BlackJack! You lose")
        return 1
    elif value1 == 21 and value2 == 21:
        print("Tie! Player and Dealer BlackJack!")
        return 1
    else:
        return 0
quit = 1
# print("How many decks would you like to play with?")
dealerdone = 0
difficulty = 1
maindeck = deck(difficulty)
while quit != 0:
    playerhand = []
    dealerhand = []
    playerhand.append(maindeck.hit())
    dealerhand.append(maindeck.hit())
    playerhand.append(maindeck.hit())
    dealerhand.append(maindeck.hit())
    playerhandvalue = calculatehandvalue(playerhand)
    playerhandvalue = checkforace(playerhand,playerhandvalue)
    dealerhandvalue = calculatehandvalue(dealerhand)
    dealerhandvalue = checkforace(dealerhand,dealerhandvalue)
    print("Dealer shows",dealerhand[1])
    print("Your hand",playerhand,"Hand =",playerhandvalue)
    gameover = checkforbj(playerhandvalue,dealerhandvalue)
    if gameover == 0:
        hit = "h"
    else:
        hit = "s"
        dealerdone = 1
    while hit == "h":
        if playerhandvalue < 21:
            print("Press h to hit or s to stay")
            hit = input()
            if hit == "h":
                playerhand.append(maindeck.hit())
                playerhandvalue = calculatehandvalue(playerhand)
                playerhandvalue = checkforace(playerhand, playerhandvalue)
                print("Your hand", playerhand, "Hand =", playerhandvalue)
        elif playerhandvalue == 21:
            hit = 'n'
        else:
            print("Player busts! Hand =",playerhandvalue)
            hit = 'n'
            gameover = 1
            dealerdone = 1

    print("Dealer shows",dealerhand,"Hand =",dealerhandvalue)

    while dealerdone == 0:
        if dealerhandvalue < 17:
            print("Dealer hits")
            dealerhand.append(maindeck.hit())
            dealerhandvalue = calculatehandvalue(dealerhand)
            dealerhandvalue = checkforace(dealerhand, dealerhandvalue)
            print("Dealer shows",dealerhand,"Hand =",dealerhandvalue)
        elif dealerhandvalue > 21:
            print("Dealer Bust! Hand =",dealerhandvalue)
            dealerdone = 1
            gameover = 1
        elif dealerhandvalue == 21:
            gameover = 0
            dealerdone = 1
        else:
            dealerdone = 1

    if gameover == 0:
        if playerhandvalue > dealerhandvalue:
            print("You Win!")
            gameover = 1
        elif playerhandvalue == dealerhandvalue:
            print("Tie")
            gameover = 1
        else:
            print("You lose!")
            gameover = 1
    print("Press any key to continue. Press 0 to quit.")
    quit = input()















