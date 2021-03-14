arr = [10, 15, 3, 7]
target = 17

def target_possible(arr, target):
    arr = set(arr)
    for num in arr:
        if target - num in arr:
            return True
    return False
            
assert target_possible(arr, target) ==  True
