def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.memoize(n)

    def memoize(self, n: int) -> {}:
        cache = {0:0, 1:1}

        for i in range(2, n+1):
            cache[i] = cache[i-1] + cache[i-2]

        return cache[n]
