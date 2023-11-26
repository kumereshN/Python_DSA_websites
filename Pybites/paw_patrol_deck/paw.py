from collections import namedtuple
from string import ascii_uppercase
import random

ACTIONS = ['draw_card', 'play_again',
           'interchange_cards', 'change_turn_direction']
NUMBERS = range(1, 5)

PawCard = namedtuple('PawCard', 'card action')

def create_paw_deck(n=8):
    if n > 26:
        raise ValueError("n cannot be more than 26")
    
    deck = list()
    required_letters = ascii_uppercase[:n]

    for letter in required_letters:
        for num in NUMBERS:
            card = PawCard(letter + str(num), None)
            deck.append(card)
    return deck

print(create_paw_deck(4)) 