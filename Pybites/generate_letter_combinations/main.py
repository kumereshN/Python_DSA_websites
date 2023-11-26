from typing import List
def generate_letter_combinations(digits: str) -> List[str]:
    """
    Calculate all possible letter combinations of a very short phone number.
    Input: A string of up to four digits.
    Output: A list of strings where each string represents a valid combination of letters
        that can be formed from the input. The strings in the output list should be sorted
        in lexicographical order.
    Raises: `ValueError`: If the input `digits` string contains non-digit characters or
        has more than four digits.
    """
    DIGITS = {
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz"
    }

    if len(digits) > 4 or any([n.isdigit() == False for n in digits]):
        raise ValueError("Digits either contain non-digit characters or has more than 4 digits")
    
    res = []
    n = len(digits)

    def dfs(i, digits, carry):
        if i == n:
            res.append(''.join(carry))
            return
        
        digit = digits[i]
        letters = DIGITS[digit]

        for letter in letters:
            dfs(i+1, digits, carry + [letter])

    dfs(0, digits, [])
    return res




if __name__ == "__main__":
    print(generate_letter_combinations("79"))