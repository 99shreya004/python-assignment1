def count_occurrences_loop(lst, x):
    count = 0
    for ele in lst:
        if ele == x:
            count += 1
    return count

my_list = [8, 6, 8, 10, 8, 20, 10, 8, 8]
element = 8
print(f"{element} has occurred {count_occurrences_loop(my_list, element)} times")
