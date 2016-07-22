def sum_of_digits(A):
    joined = ''
    sum = 0
    for each in A:
        joined += str(each)

    for num in joined:
        sum += int(num)
    return sum
