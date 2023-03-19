from typing import Dict
import re

table = {'*': 'c',

             '#': '00',

             '$': '*y',

             }

""" table = {'#': 'hem',
             '@': 'T#',
             '$': 't#',
             '&': '$ as',
             '*': ' do ',
             '%': ' to',
             '^': ' someone ',
             '~': 'for ',
             '+': '~&',
             } """

expanded_table = dict()

def check_and_replace_special_chars(key:str, val: str, table: Dict[str, str]) -> str:
    pattern = '[^a-zA-Z0-9 ]'
    flag = True
    p = re.compile(pattern)
    

    while flag:
        if bool(p.search(val)) == True:
            special_char = p.search(val)[0]
            val = val.replace(special_char, table[special_char])
        else:
            flag = False
    return val


for key, val in table.items():
    val = check_and_replace_special_chars(key, val, table)
    expanded_table[key] = val


s1 = "@ as can*has%*+ can't. And^has% speak up + has no voices."
s2 = "$3#"

for key, val in expanded_table.items():
    if key in s2:
        s2 = s2.replace(key, expanded_table[key])

print(s2)