"""
Depth-first search is an algorithm for traversing or searching tree or 
graph data structures.
The basic idea is to start from the root or any arbitrary node and
mark the node and move to the adjacent unmarked node and continue this
loop until there is no unmarked adjacent node. Then backtrack and check 
for other unmarked nodes and traverse them.

Time complexity:	O(V+E)
Space complexity:	O(V)
"""
from graph import graph, root

def search(graph, item):
	search_queue = list()
	search_queue += graph[root]

	print("Pop", root)
	print("Add", search_queue)
	print("Search queue:", *search_queue)
	
	searched = set()
	while search_queue:
		i = search_queue.pop(0)
		print("Pop", i)

		if i not in searched:
			if i == item:
				print("found")
				return True
			else:
				searched.add(i)
				search_queue += graph[i]

				print("Add", graph[i])
				print("Search queue", *search_queue)
		else:
			print("Already searched")
	
	return False

search(graph, 9)