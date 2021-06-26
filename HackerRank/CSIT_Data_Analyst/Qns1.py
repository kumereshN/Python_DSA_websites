# Answer (Negative stepback)
import string
symbols_low = string.ascii_lowercase
symbols_up = string.ascii_uppercase

def caesarCipher(s, k):
    res = []
    for c in s:
        if c.isupper():
            res.append(symbols_up[(symbols_up.index(c)-k)%len(symbols_up)]) # If the index number > 26, then % len(symbols_up) will get the remainder which will move the index back to the beginning of the symbols_up.
        elif c.islower():
            res.append(symbols_low[(symbols_low.index(c)-k)%len(symbols_low)])
        else:
            res.append(c)

    return "".join(map(str, res))


encrypted = "VTAOG"
k = 2
caesarCipher(encrypted,k)

import string
def simpleCipher(encrypted, k):
    d = {ch: n for n, ch in enumerate(string.ascii_uppercase)} # Dict of chars
    decrypt_str = ""

    for ch in encrypted:
        target_idx = d[ch]
        target_idx -= 2
        if target_idx < 0:
            target_idx += 26
            for key, value in d.items():
                if target_idx == value:
                    decrypt_str += key
        else:
            target_idx -= 2
            for key, value in d.items():
                if target_idx == value:
                    decrypt_str += key
    return decrypt_str

encrypted = "VTAOG"
k = 2
simpleCipher(encrypted,k)


# Answer
import string
symbols_low = string.ascii_lowercase
symbols_up = string.ascii_uppercase

def caesarCipher(s, k):
    res = []
    for c in s:
        if c.isupper():
            res.append(symbols_up[(symbols_up.index(c)+k)%len(symbols_up)])
        elif c.islower():
            res.append(symbols_low[(symbols_low.index(c)+k)%len(symbols_low)])
        else:
            res.append(c)

    return "".join(map(str, res))
