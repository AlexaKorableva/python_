

def fibonacci(n, m):
    fib = []
    a, b = 1, 1
    for num in range(m):
        fib.append(b)
        a, b = b, a+b
    n -= 1
    res = [fib[i] for i in range(n, m)]
    del fib
    print(res)
    return res

n= 5
m=12
fibonacci(n, m)
