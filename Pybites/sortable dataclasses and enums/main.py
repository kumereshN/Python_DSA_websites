from dataclasses import dataclass
import enum
from typing import List  # TODO: can remove >= 3.9
import operator


# 1. make a BiteLevel enum class
# keys = INTRO BEGINNER INTERMEDIATE ADVANCED
# values = 1 2 3 4
# make sure they can be sorted by int value

class BiteLevel(enum.IntEnum):
    INTRO = 1
    BEGINNER = 2
    INTERMEDIATE = 3
    ADVANCED = 4


# 2. make a dataclass that can be ordered
# attributes: number (int), title (str), level (BiteLevel)
@dataclass(order = True)
class Bite:
    number: int
    title: str
    level: BiteLevel


# 3. complete the function below

def create_bites(numbers: List[int], titles: List[str],
                 levels: List[BiteLevel]):
    """Generate a generator of Bite dataclass objects"""
    for args in zip(numbers, titles, levels):
        yield Bite(*args)



NUMBERS = [101, 1, 97, 2]
TITLES = 'f-string,sum numbers,scrape holidays,regex fun'.split(',')
SCORES = BiteLevel.__members__.values()

bites = create_bites(NUMBERS,TITLES,SCORES)
print(sorted(bites, key=operator.attrgetter('level'),
                             reverse=True))