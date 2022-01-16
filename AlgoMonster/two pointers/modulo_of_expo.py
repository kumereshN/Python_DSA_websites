def step(n, m):
    return (n ** 2) % m

def modulo_of_exponent(n, k, m):
    k -= 1
    tortoise = step(n, m)
    hare = step(step(n, m), m)
    while k > 0 and tortoise != hare:
        k -= 1
        tortoise = step(tortoise, m)
        hare = step(step(hare, m), m)
    if k == 0:
        return tortoise
    cycle_size = 1
    tortoise = step(tortoise, m)
    hare = step(step(hare, m), m)
    k -= 1
    while k > 0 and tortoise != hare:
        tortoise = step(tortoise, m)
        hare = step(step(hare, m), m)
        k -= 1
        cycle_size += 1
    if k == 0:
        return tortoise
    k = k % cycle_size
    while k > 0:
        tortoise = step(tortoise, m)
        k -= 1
    return tortoise

n,k,m = 2,3,10
modulo_of_exponent(n,k,m)