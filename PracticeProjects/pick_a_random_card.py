'''
There are so many card games today where you choose a card at random from a deck of cards to create an event.
This is the feature of every card game today because you have to choose a card at random and once you choose a card it becomes an event.

So to pick a random card from a deck of cards, We will create two Python lists:

one for storing the suits
another for storing the ranks of cards.
Using the random module, choose a random value from the first list
Using the random module choose a random sign from the second list
Just concatenate those random value and sign

'''

import random
cards = ["Diamonds", "Spades", "Hearts", "Clubs"]
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]

def pick_a_card():
    card = random.choices(cards)
    rank = random.choices(ranks)
    return(f"The {rank} of {card}")

print(pick_a_card())
