from typing import List, TypeVar
T = TypeVar('T', int, float)


def n_digit_numbers(numbers: List[T], n: int) -> List[int]:
    if n <= 0:
        raise ValueError
    elif numbers == []:
        return numbers
    
    multiplier = n if n < 2 else int('1' + ('0' * (n-1)))

    res = []

    for number in numbers:
        number_len = len(str(number))
        if number_len == n and isinstance(number, int):
            res.append(number)
        elif isinstance(number, float) or number_len < n:
            number = int(number * multiplier)
            res.append(number)
        else:
            divisor = int('1' + ('0' * (number_len - n)))
            number = number // divisor
            res.append(number)
    
    return res



l = [-1.1, 2.22, -3.333, 4444, 55555]
n = 4
print(n_digit_numbers(l, n))