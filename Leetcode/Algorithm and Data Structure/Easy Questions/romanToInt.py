class Solution:
    def romanToInt(self, s: str) -> int:
        x = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        k = list(x.keys())
        sum = 0
        com = False
        for idx, i in enumerate(s):
            if com:
                if k.index(i) > k.index(com):
                    sum -= 2 * x[com]
            sum += x[i]
            com = i
        return sum

    def romanToInt(self, s: str) -> int:
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sum = dic[s[-1]]

        for i in range(len(s) - 1, 0, -1):
            if dic[s[i - 1]] < dic[s[i]]:  # Special cases of 4's and 9's
                sum -= dic[s[i - 1]]
            else:
                sum += dic[s[i - 1]]

        return sum
