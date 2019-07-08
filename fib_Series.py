# Fibonacci series

from functools import Lru_cache


@Lru_cache(max_Size=1000)
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(1, 100):
    print i, fibonacci(i)

# Without any usage of library(lru_Cache)
fibonacci_cache = {}


def fibonacci(n):
    # if we have cached value then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        value = fibonacci(n - 1) + fibonacci(n - 2)
    # cache the value and return it
    fibonacci_cache[n] = value
    return value


for n in range(1, 100):
    print n, fibonacci(n)
