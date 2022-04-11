def dfs_iterative(start_node, graph):
    visited = set()
    if start_node not in graph:
        print("Start Node couldn't be found. Program is existing...")
        return

    stack = [start_node]
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node)
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)


graph = {'A': ['B', 'C', 'D'],
         'B': ['A', 'E', 'D'],
         'C': ['A', 'D'],
         'D': ['A', 'B', 'C', 'E'],
         'E': ['B', 'D']
         }
dfs_iterative('A', graph)
