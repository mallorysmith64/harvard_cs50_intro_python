from random import choice
from random import randint
from random import shuffle

coin = choice(["heads", "tails"])
print("You flipped", coin)

number = randint(1,10)
print(number)

cards = ["jack", "queen", "king"]
shuffle(cards)
for card in cards:
    print(card)