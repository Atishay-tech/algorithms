"""
The binary_search function takes a sorted array and an item. If the
item is in the array, the function returns its position.

Time complexity:
Best-case:      O(1)
Average-case:   O(log n)
Worst-case:     O(log n)

Worst-case space complexity: O(1)
"""
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


def show_status(lst, low, high, mid):
    print(*lst[low : high+1], end='\t\t')
    print("Mid = {}".format(lst[mid]))


lst = [1, 3, 6, 9, 16, 19, 23, 24]
item = 23
print("\nGiven sorted Array: {}\nItem: {}\n".format(lst, item))
print("Binary Sorting:")
print("\nItem Index:", binary_search(lst, item))