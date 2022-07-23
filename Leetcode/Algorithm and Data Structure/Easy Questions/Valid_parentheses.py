def isValid(s: str) -> bool:
    stack = [0]
    hashmap = {0: None, "(": ")", "[": "]", "{": "}"}

    for char in s:
        if char in hashmap:
            stack.append(char)
        else:
            if hashmap[stack.pop()] != char:
                return False
    return stack == [0]

s = "()"
print(isValid(s))


# def isValid(self, s: str) -> bool:
#     if len(s) <= 1:
#         return False

#     stack = []
#     for ch in s:
#         # If open brackets, push onto the stack
#         if ch == '(' or ch == '{' or ch == '[':
#             stack.append(ch)
#         # if close ')' pop and compare the pair to be opposite version of it
#         elif ch == ')' and stack and stack.pop() == '(':
#             continue
#         # if close '}' pop and compare the pair to be opposite version of it
#         elif ch == '}' and stack and stack.pop() == '{':
#             continue
#         # if close ']' pop and compare the pair to be opposite version of it
#         elif ch == ']' and stack and stack.pop() == '[':
#             continue
#         # If the above condition is not true, then its not valid
#         else:
#             return False


# # Alternative
# def isValid(self, s: str) -> bool:
#         stack = []
#         for i in s:
#             if len(stack) == 0:
#                 stack.append(i)
#             elif stack[-1] == '{' and i == '}': # If the last bracket is equal to i
#                 stack.pop() # Remove the last bracket in the stack
#             elif stack[-1] == '(' and i == ')':
#                 stack.pop()
#             elif stack[-1] == '[' and i == ']':
#                 stack.pop()
#             else:
#                 stack.append(i)
#         return False if stack else True
