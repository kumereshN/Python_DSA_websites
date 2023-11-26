res = []
def dfs(lst_of_lst):
    for c in lst_of_lst:
        if isinstance(c, (list, tuple)):
            dfs(c)
        else:
            res.append(c)
    return res


lst = [1, (2, 3), [(4, 5), [6, 7, [8, 9, 10]]]]
print(dfs(lst))