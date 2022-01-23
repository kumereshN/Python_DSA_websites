from collections import Counter
from heapq import heappush, heappop

def reorganizeString(s):   
	if not s:
		return ""
	# Build freq dict:
	d = Counter(s)

	# push (-ve frq, char) pairs into heap
	h = []
	for k in d:
		heappush(h, (-d[k], k))

	res = ""
	# pop and examine frq and append to res
	while len(h) > 1:        # -------------------------------- NOTE [1]
		f1, c1 = heappop(h)
		f2, c2 = heappop(h)

		res += c1
		res += c2

		if abs(f1) > 1: # if char repeats
			heappush(h, (f1+1, c1)) # push back with decrement frq

		if abs(f2) > 1: 
			heappush(h, (f2+1, c2)) # push back with decrement frq


	if h:     # -------------------------------- NOTE [2]
		f, c = h[0]
		if abs(f) > 1: 
			return "" # this means we have something like h = [(2, "a")] which means there is no escape from repeating same char in text
		else:
			res += c
	return res

s = "aab"
reorganizeString(s)


# Source: https://leetcode.com/problems/reorganize-string/discuss/492827/Python-Simple-heap-solution-with-detailed-explanation