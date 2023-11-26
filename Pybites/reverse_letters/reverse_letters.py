from string import ascii_letters

def reverse_letters(string: str) -> str:
    left = 0
    right = len(string)-1
    stack = [c for c in string]

    while left < right:
        left_ch, right_ch = stack[left], stack[right]
        if left_ch in ascii_letters and right_ch in ascii_letters:
            stack[left], stack[right] = stack[right], stack[left]
            left += 1
            right -= 1
        elif left_ch in ascii_letters:
            right -= 1
        else:
            left += 1
    return "".join(stack)


if __name__ == "__main__":
    reverse_letters()