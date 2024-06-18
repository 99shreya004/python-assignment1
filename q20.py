def sumOfList(lst, size):
    if size == 0:
        return 0
    else:
        return lst[size - 1] + sumOfList(lst, size - 1)

list1 = [11, 5, 17, 18, 23]
total = sumOfList(list1, len(list1))
print("Sum of all elements in the given list:", total)
