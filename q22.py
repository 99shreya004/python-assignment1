def find_min_max(lst):
    min_val = lst[0]
    max_val = lst[0]
    for num in lst:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num
    return min_val, max_val

numbers = [3, 1, 4, 1, 5, 9, 2]
min_num, max_num = find_min_max(numbers)
print("Minimum:", min_num, "Maximum:", max_num)
