"""
QuickSort is a highly efficient sorting algorithm based on Divide and Conquer approach.
A large array is partitioned into two arrays one of which holds values smaller than the specified value, say pivot,
based on which the partition is made and another array holds values greater than the pivot value.

Quicksort partitions an array and then calls itself recursively twice to sort the two resulting subarrays.

Time complexity:
Best-case:      O(n*logn)
Average-case:   O(n*logn)
Worst-case:     O(n^2)

Worst-case space complexity: O(n)
"""

def print_status(lower: list, pivot: int, upper: list) -> None:
	print("Pivot:", pivot)
	print("Lower:", *lower)
	print("Upper:", *upper)
	print()


def quick_sort(arr: list) -> list:
	if len(arr) < 2:
		return arr

	else:
		mid = len(arr) // 2
		pivot = arr[mid]
		lower = list()
		higher = list()

		for i in range(len(arr)):
			if arr[i] < pivot:
				lower.append(arr[i])
			elif arr[i] > pivot:
				higher.append(arr[i])
			elif i != mid:
				lower.append(arr[i])

		# For showing working of algorithm
		print_status(lower, pivot, higher)

		return quick_sort(lower) + [pivot] + quick_sort(higher)


arr = [2, 1, 5, 1, 3, 9, 1 , 8, 13]
print("Given Array:")
print(*arr)
print()
arr = quick_sort(arr)
print("Sorted Array:")
print(*arr)
