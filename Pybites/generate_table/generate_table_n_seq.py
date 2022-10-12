import random

def generate_table(name_lst = None, alias_lst = None, points_lst = None, awake_lst = None, sep = None):
    
    def check_for_params(name = None, alias = None, points = None, awake = None):
        
        req_params = []
        
        for param in params:
            if param:
                req_params.append(param)
        return req_params

    def check_if_str(param_lst):
        updated_param_lst = []
        
        for param in param_lst:
            if not all(isinstance(item, str) for item in param):
                updated_param_lst.append([str(x) for x in param])
            else:
                updated_param_lst.append(param)
        return updated_param_lst
    
    params = [name_lst, alias_lst, points_lst, awake_lst]
    req_params = check_if_str(check_for_params(*params))
    
    if len(req_params) != 1:
        z = list(zip(*req_params))
        result = [SEPARATOR.join(x) for x in z]
        return result
    else:
        return req_params.pop()
    
names = ['Julian', 'Bob', 'PyBites', 'Dante', 'Martin', 'Rodolfo']
aliases = ['Pythonista', 'Nerd', 'Coder'] * 2
points = random.sample(range(81, 101), 6)
awake = [True, False] * 3
SEPARATOR = ' | '

# generate_table(names, aliases, points, awake)