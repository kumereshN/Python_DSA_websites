def longestValidParentheses(self, s: str) -> int:
        stack = [0,] # Initial value to handle "()"
        max_parenthesis = 0
        for bracket in s:
            if bracket == '(':
                stack.append(0)
            else:
                if len(stack) > 1:
                    val = stack.pop()
                    stack[-1] += val + 2  # Add 2 when a ")" matches "("
                    max_parenthesis = max(max_parenthesis, stack[-1]) # Keep track of longest valid sequence
                else:
                    stack = [0]

        return max_parenthesis
