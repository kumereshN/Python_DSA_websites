import random

MAX_GUESSES = 5
START, END = 1, 20


def get_random_number():
    """Get a random number between START and END, returns int"""
    return random.randint(START, END)


class Game:
    """Number guess class, make it callable to initiate game"""

    def __init__(self):
        """Init _guesses, _answer, _win to set(), get_random_number(), False"""
        self._guesses = MAX_GUESSES
        self._answer = get_random_number()
        self._win = None
        self._user_guessed_number = -1
        self._already_guessed_numbers = set()
        self._range_of_numbers = range(START, END+1)

    def guess(self):
        """Ask user for input, convert to int, raise ValueError outputting
           the following errors when applicable:
           'Please enter a number'
           'Should be a number'
           'Number not in range'
           'Already guessed'
           If all good, return the int"""
        user_guess_no = input("Guess a number between 1 and 20: ")
        try:
            self._user_guessed_number = int(user_guess_no)
        except (TypeError, ValueError):
            print("Please enter a number")
            raise ValueError("Please enter a number")
        
        if self._user_guessed_number in self._already_guessed_numbers:
            print("Already guessed")
            raise ValueError("Already guessed")
        if self._user_guessed_number not in self._range_of_numbers:
            print("Number not in range")
            raise ValueError("Number not in range")
        
        self._already_guessed_numbers.add(self._user_guessed_number)
        
        return self._user_guessed_number

    def _validate_guess(self, guess):
        """Verify if guess is correct, print the following when applicable:
           {guess} is correct!
           {guess} is too low
           {guess} is too high
           Return a boolean"""
        if guess == self._answer:
            print(f"{guess} is correct!")
            return True
        elif guess > self._answer:
            print(f"{guess} is too high")
            return False
        else:
            print(f"{guess} is too low")
            return False

    def __call__(self):
        """Entry point / game loop, use a loop break/continue,
           see the tests for the exact win/lose messaging"""
        while self._guesses > 0:
            try:
                user_guessed_number = self.guess()
                self._win = self._validate_guess(user_guessed_number)
                if self._win:
                    guesses_str = self._guesses == 1 and "guess" or "guesses"
                    print(f"It took you {self._guesses} {guesses_str}")
                    break
            except Exception:
                self._guesses -= 1
                continue
        
        print(f'Guessed {MAX_GUESSES} times, answer was {self._answer}')
        


if __name__ == '__main__':
    game = Game()
    game() 