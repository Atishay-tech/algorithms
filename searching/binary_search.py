def show_status(lst, low, high, mid):
    print(*lst[low : high+1], end='\t\t')
    print("Mid = {}".format(lst[mid]))


def binary_search(lst, item):
    low, high = 0, len(lst)-1

    while low <= high:
        mid = (low + high) // 2
        guess = lst[mid]

        # Just for showing the working
        show_status(lst, low, high, mid)
        
        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        elif guess > item:
            high = mid - 1

    return None     # Item not found


lst = [1, 3, 6, 9, 16, 19, 23, 24]
item = 23
print("\nGiven sorted Array: {}\nItem: {}\n".format(lst, item))
print("Binary Sorting:")
print("\nIndex found:", binary_search(lst, item))