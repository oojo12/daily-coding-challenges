def find_max_of_three(item_list):
    item_list = sorted(item_list)
    if item_list[-1] * item_list[-2] > item_list[0]*item_list[1]:
        return item_list[-1] * item_list[-2] * item_list[-3]
    else:
        return item_list[0] * item_list[1] * item_list[-1]
