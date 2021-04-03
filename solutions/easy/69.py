def find_max_of_three(item):
    item = sorted(item)
    # case 1: most negative > most positive and max is non-negative
    if item[0] * item[1] > item[-1] * item[-2] and item[-1] >= 0:
        return item[0] * item[1] * item[-1]
    # case 2: most negative > most positive and max is negative
    elif item[0] * item[1] > item[-1] * item[-2] and item[-1] < 0:
        return item[-1] * item[-2] * item[-3]
    # case 3: most negative < most positive
    else:
        return item[-1] * item[-2] * item[-3]

assert 500 == find_max_of_three([-10, -10, 5, 2])
assert 2000 == find_max_of_three([-20, -10, 5, 10])
assert 1000 == find_max_of_three([-20, 10, 10, 10])
assert 2000 == find_max_of_three([-20, -10, -10, 10])
assert -2000 == find_max_of_three([20, -10, -10, 10])
