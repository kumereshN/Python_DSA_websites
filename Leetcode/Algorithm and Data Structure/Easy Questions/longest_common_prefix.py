class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix_str = ""

        if not strs:
            return prefix_str

        for s in zip(*strs):
            if len(set(s)) != 1:
                return prefix_str
            else:
                prefix_str += s[0]

        return prefix_str


# Alternative solution
def longestCommonPrefix(strs):
    if not strs:
        return ""

    prefix = ""
    for i in range(min(map(len, strs))):
        ch = strs[0][i]
        if all(s[i] == ch for s in strs):
            prefix += ch
        else:
            break
    return prefix


strs = ["flower", "flow", "flight"]
longestCommonPrefix(strs)


# Alternative solution
def longestCommonPrefix(strs):
    res, i, j = "", 0, 0
    try:
        while True:
            if i == len(strs) - 1:
                res += strs[0][j]
                i = 0
                j += 1
            if strs[i][j] == strs[i + 1][j]:
                i += 1
            else:
                return res
    except:
        return res
