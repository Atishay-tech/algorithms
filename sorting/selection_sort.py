"""
The selection sort algorithm is an in-place algorithm in which the 
list is divided in to two parts, the sorted part at the left and
the unsorted part at the right end. Initially the soted part is empty
and the unsorted part is the entire list.
The smallest element is selected from the unsorted part and swapped with
its leftmost element, and the element becomes the part of the sorted
array. This process continues increasing sorted list's boundary one
element to the right.

Time complexity:
Best-case:      O(n^2)
Average-case:   O(n^2)
Worst-case:     O(n^2)

Worst-case space complexity: O(1)
"""

def minimum(arr, i):
	"""Returns the index of smallest element in array"""
	smallest = i
	for j in range(i+1, len(arr)):
		if arr[j] < arr[smallest]:
			smallest = j
	return smallest


def selection_sort(arr):
	for i in range(len(arr)):
		smallest = minimum(arr, i)

		# Showing the working of algorithm
		show_status(arr, smallest)

		arr[i], arr[smallest] = arr[smallest], arr[i]


def show_status(arr, smallest):
	print(*arr, "\tMin: ", arr[smallest])


arr = [67, 15, 6, 1 ,31, 23, 10, 23]
print("Given array:\n", *arr)
print("\nSelection Sort:")
selection_sort(arr)
print("\nSorted array:\n", *arr)
