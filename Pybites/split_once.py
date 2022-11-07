from string import whitespace
from typing import List


def split_once(text: str, separators: str = None) -> List[str]:
    result, buffer = [], []
    # Create a set around the separators (If it's not None) or the whitespace
    separators = set(separators or whitespace)

    for ch in text:
        try:
            # Attempt to find and remove the seperator from the seperator set
            separators.remove(ch)
        except KeyError:
            # If it's not part of the seperator set, append the ch to buffer to hold the characters.
            buffer.append(ch)
        else:
            # Once it finds a seperator in the string, append the buffer to the result list
            result.append(''.join(buffer))
            # clear the buffer to hold the next part of the string
            buffer.clear()
    
    # The remaining string in the buffer will be appended to result (list)
    result.append(''.join(buffer))
    return result