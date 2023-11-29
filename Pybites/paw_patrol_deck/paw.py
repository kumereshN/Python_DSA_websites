from collections import namedtuple
from string import ascii_uppercase
import random

ACTIONS = ['draw_card', 'play_again',
           'interchange_cards', 'change_turn_direction']
NUMBERS = range(1, 5)

PawCard = namedtuple('PawCard', 'card action')

def generate_random_numbers(total_action_cards, total_cards):
    random_seq = set()
    while len(random_seq) < total_action_cards:
        random_no = random.randint(0, total_cards)
        random_seq.add(random_no)
    return random_seq

def create_paw_deck(n=8):
    if n > 26:
        raise ValueError("n cannot be more than 26")
    
    deck = list()
    required_letters = ascii_uppercase[:n]
    total_actions = [2 for _ in range(4)]
    actions_counter = dict(zip(ACTIONS, total_actions))

    random_no_seq = generate_random_numbers(8, n * 4)

    for letter in required_letters:
        idx_of_random_no = random_no_seq.pop()
        for num in NUMBERS:
            if idx_of_random_no % 4 == num or idx_of_random_no % 4 == 0:
                random_action_card = random.choice(ACTIONS)
                card = PawCard(letter + str(num), random_action_card)
                idx_of_random_no = random_no_seq.pop()
            else:
                card = PawCard(letter + str(num), None)
            deck.append(card)
    return deck

print(create_paw_deck(4))



# print(generate_random_numbers(8, 16))