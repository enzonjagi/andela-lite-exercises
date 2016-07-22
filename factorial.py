def factorial(n):
    f = []
    while n > 1:
        for x in range(1,10):
            if n % x == 0:
                if x in f:
                    x += 1
                else:
                    f.append(x)
                    return f
            else:
                x = x + 1


v = 25
factorial(v)
