from collections import namedtuple
from string import ascii_uppercase
import heapq
import random

ACTIONS = ['draw_card', 'play_again',
           'interchange_cards', 'change_turn_direction']
NUMBERS = range(1, 5)

PawCard = namedtuple('PawCard', 'card action')

def generate_random_numbers(total_action_cards, total_cards):
    random_seq = set()
    while len(random_seq) < total_action_cards:
        random_no = random.randint(0, total_cards-1)
        random_seq.add(random_no)
    random_seq = list(random_seq)
    heapq.heapify(random_seq)
    return random_seq

def create_paw_deck(n=8):
    if n > 26:
        raise ValueError("n cannot be more than 26")
    
    deck = list()
    required_letters = ascii_uppercase[:n]
    ACTIONS_LST = ACTIONS * (n // 4) if n > 3 else ACTIONS
    random.shuffle(ACTIONS_LST)

    random_no_seq = generate_random_numbers(n, n * 4)
    action_and_index = dict(zip(random_no_seq, ACTIONS_LST))
    card_idx = 0

    idx_of_random_no = heapq.heappop(random_no_seq)

    for letter in required_letters:
        for card_num in NUMBERS:
            # Assign an ACTION
            if idx_of_random_no == card_idx:
                random_action_card = action_and_index.get(idx_of_random_no, None)
                card = PawCard(letter + str(card_num), random_action_card)
                idx_of_random_no = heapq.heappop(random_no_seq) if len(random_no_seq) > 0 else -1
                card_idx += 1
            else:
                card = PawCard(letter + str(card_num), None)
                card_idx += 1
            deck.append(card)
    return deck

print(create_paw_deck(16))


# n = 4
# print(generate_random_numbers(n, n * 4))