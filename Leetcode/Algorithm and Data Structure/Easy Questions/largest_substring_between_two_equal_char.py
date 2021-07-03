def maxLengthBetweenEqualCharacters(s):
    hashmap, ans = dict(), -1

    for idx, ch in enumerate(s):
        if ch in hashmap:
            ans = max(ans, idx - hashmap[ch] - 1)
        else:
            hashmap[ch] = idx
    return ans


s = "ojdncpvyneq"
maxLengthBetweenEqualCharacters(s)
