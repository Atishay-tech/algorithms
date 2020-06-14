"""
Dijkstra's algorithm allows us to find the shortest path between any
two vertices of a graph.
Dijkstra's Algorithm works on the basis that any subpath B -> D of the
shortest path A -> D between vertices A and D is also the shortest path
between vertices B and D.

Time Complexity: O(E Log V)
Space Complexity: O(V)
where, E is the number of edges and V is the number of vertices.
"""
parents = {}
visited = []
inf = float("inf")

# Weighted directed Graph implemented using dictionary.
graph = {}
graph['a'] = {}
graph['a']['b'] = 1
graph['a']['c'] = 2
graph['b'] = {}
graph['b']['a'] = 2
graph['c'] = {}
graph['c']['d'] = 4
graph['c']['f'] = 2
graph['d'] = {}
graph['d']['b'] = 2
graph['d']['e'] = 3
graph['e'] = {}
graph['e']['f'] = 1
graph['f'] = {}


def dijkstra(start: str, end: str) -> int:
    print('Start:', start)
    print('End:', end )

    # Initializing cost table
    costs = {}
    for node in graph:
        costs[node] = inf
    costs[start] = 0
    parents[start] = None

    # Working algorithm
    node = start
    while node is not None:
        print('\nCosts:', sorted(costs.items()))
        print('Node', node)
        print('Neighbours:')
        visited.append(node)
        for neighbour in graph[node]:
            new_cost = min(
                costs[neighbour],
                costs[node] + graph[node][neighbour])

            if new_cost < costs[neighbour]:
                costs[neighbour] = new_cost
                parents[neighbour] = node

            print('Edge {} {} = {}'.format(
                    node, neighbour, graph[node][neighbour])
                )

        print('Visited: {}'.format(visited))
        print('Parents:')
        for node in parents:
            print(node, ':', parents[node])
        node = find_lowest_cost_node(costs)

    return costs[end]


def find_lowest_cost_node(costs: dict) -> str:
    min_cost = inf
    min_node = None
    for node in costs:
        if (node not in visited) and (costs[node] < min_cost):
            min_node = node
            min_cost = costs[node]
    return min_node


def print_path(start:str, end:str) -> None:
    path = []
    parent = end
    while parent is not None:
        path.append(parent)
        parent = parents[parent]
    path.reverse()
    print(*path, sep=' -> ')


if __name__ == '__main__':
    start = 'a'
    end = 'f'
    print('\nMinimum cost = ', dijkstra(start, end))
    print_path(start, end)



