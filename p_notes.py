# memoization example

# fibonacci1 is inefficient

def fibonacci1(n):
    if n in [0,1]:
        return n
    return fibonacci1(n-1) + fibonacci1(n-2)

# print(fibonacci1(100))
# => takes forever

# function calls itself twice for values > 2 for each recursive step
# solution: cache values

def fibonacci2(n):
    cache = {}
    print('cache is now: ', cache)
    def inner(m):
        if m in [0,1]:
            return m
        if m not in cache:
            cache[m] = inner(m-1) + inner(m-2)
        print('cache in inner: ', cache)
        return cache[m]
    return inner(n)

# print(fibonacci2(100))

# faster to insert cache into function argument as default value

def fibonacci3(n, cache={ 0:0, 1:1 }):
    def inner(m):
        if m not in cache:
            cache[m] = inner(m-1) + inner(m-2)
        return cache[m]
    return inner(n)