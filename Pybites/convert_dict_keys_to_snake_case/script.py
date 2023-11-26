import re

def snake_case_keys(data):

    def convert_to_snake_case(s: str) -> str:
        regex_check_for_caps_and_numbers = re.compile('(?!^)([A-Z-]|\d+)')
        s = re.sub(regex_check_for_caps_and_numbers, r'_\1', key).lower().replace('-','')
        return s

    res_dict = dict()

    if isinstance(data, dict):
        for key, value in data.items():
            key = convert_to_snake_case(key)
            if isinstance(value, dict) or isinstance(value, list):
                value = snake_case_keys(value)

            res_dict[key] = value
        return res_dict
    elif isinstance(data, list):
        lst = []
        for d in data:
            value = snake_case_keys(d)
            lst.append(value)
        return lst
    else:
        return data

    


data = {
        "random": [
            "Luke",
            [
                "blowing up the death star",
                {"skillName": "bulls-eye womprats",
                 "skillParameters": "with my T47"},
            ],
        ]
    }
print(snake_case_keys(data))