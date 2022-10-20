from typing import List

def generate_parentheses(n: int) -> List[str]:
    # WRITE YOUR BRILLIANT CODE HERE
    ret = []
    
    def backtrack(n, openParen, curr):
        # If the number of matching parentheses AND open parentheses reaches 0, then we've found a combination matching pair
        if n == 0 and openParen == 0:
            ret.append(curr)
            return
        # If there is still n matching parentheses to be filled up, then continue adding the open paretheses.
        if n > 0:
            backtrack(n - 1, openParen + 1, curr + '(')
        # After n reaches 0, we've to add the closing parenthense to complete the matching parentheses.
        if openParen > 0:
            backtrack(n, openParen - 1, curr + ')')
            
    backtrack(n, 0, '')
    return ret

n = 2

print(generate_parentheses(n))