from typing import List


def letter_combinations_of_phone_number(digits: str) -> List[str]:
    # WRITE YOUR BRILLIANT CODE HERE
    KEYBOARD = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    res = []

    def dfs(path):
        # Base case
        if len(path) == len(digits):
            res.append(''.join(path))
            return

        # Getting the digit
        next_number = digits[len(path)]
        # getting each letter from the string of letters
        for letter in KEYBOARD[next_number]:
            path.append(letter)
            dfs(path)
            path.pop()

    dfs([])
    return res

"""
Alternative: without using append and pop methods
"""

def letter_combinations_of_phone_number(digits: str) -> List[str]:
    # WRITE YOUR BRILLIANT CODE HERE
    KEYBOARD = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    res = []

    def dfs(path):
        # Base case
        if len(path) == len(digits):
            res.append(''.join(path))
            return

        # Getting the digit
        next_number = digits[len(path)]
        # getting each letter from the string of letters
        for letter in KEYBOARD[next_number]:
            dfs(path + [letter])

    dfs([])
    return res

if __name__ == '__main__':
    digits = input()
    res = letter_combinations_of_phone_number(digits)
    print(' '.join(res))


"""
Alternative 2: without using append and pop methods
"""

def letter_combinations_of_phone_number(digits: str) -> List[str]:
    # WRITE YOUR BRILLIANT CODE HERE
    KEYBOARD = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    res = []

    def dfs(i, path):
        # Base case
        if len(path) == len(digits):
            res.append(''.join(path))
            return

        # Getting the digit
        next_number = digits[i]
        # getting each letter from the string of letters
        for letter in KEYBOARD[next_number]:
            # i+1 means getting the index of the next digit
            dfs(i+1, path + [letter])

    dfs([])
    return res

if __name__ == '__main__':
    digits = input()
    res = letter_combinations_of_phone_number(digits)
    print(' '.join(res))
