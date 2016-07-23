def factorial1(n):
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
factorial1(v)

def factorial2(n):
    f = []
    while n > 1:
        for x in range(1,10):
            if n % x == 0:
                n /= x
                return n
                if x in f:
                    x += 1
                else:
                    f.append(x)
                    return f
            else:
                x += 1

d = 250
factorial2(d)
