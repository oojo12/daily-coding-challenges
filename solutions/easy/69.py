#FIX FAILS 4TH ASSERTION
def find_max_of_three(item_list):
    item_list = sorted(item_list)
    if item_list[-1] * item_list[-2] > item_list[0]*item_list[1]:
        return item_list[-1] * item_list[-2] * item_list[-3]
    else:
        return item_list[0] * item_list[1] * item_list[-1]

assert 500 == find_max_of_three([-10, -10, 5, 2])
assert 2000 == find_max_of_three([-20, -10, 5, 10])
assert 1000 == find_max_of_three([-20, 10, 10, 10])
assert -1000 == find_max_of_three([-20, -10, -10, 10])
