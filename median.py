def median(lst):
    new_lst = sorted(lst)
    half_loc = len(new_lst) // 2
    if len(lst) % 2 != 0:
        result = new_lst[half_loc]
    else:
        result = (new_lst[half_loc] + new_lst[half_loc - 1]) / 2.0
    print (new_lst)
    return result

print(median([7, 12, 3, 1, 6, 8, 9, 10]))