def sum_of_unique_digits(A):
    added = ''
    chosen = ''
    sum = 0
    for each in A:
        added += str(each)

    for num in added:
        if num not in chosen:
            chosen += num
    for num in chosen:
        sum += int(num)
    return sum
