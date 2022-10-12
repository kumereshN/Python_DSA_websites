import random
from tkinter import SW

names = ['Julian', 'Bob', 'PyBites', 'Dante', 'Martin', 'Rodolfo']
aliases = ['Pythonista', 'Nerd', 'Coder'] * 2
points = random.sample(range(81, 101), 6)
awake = [True, False] * 3
SEPARATOR = ' | '


def generate_table(*sequences):
    for seq in zip(*sequences):
        seq = [str(val) for val in seq]
        yield SEPARATOR.join(seq)
    
generate_table(names, aliases, points)