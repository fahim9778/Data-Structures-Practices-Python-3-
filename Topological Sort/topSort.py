class Graph:
    def __init__(self, vertices, is_directed=False):
        self.vertices = vertices
        self.adj_list = {}
        self.is_directed = is_directed

        for vertex in self.vertices:
            self.adj_list[vertex] = []

    def add_edge(self, source, destination):
        self.adj_list[source].append(destination)
        if not self.is_directed:
            self.adj_list[destination].append(source)

    def print_adj_list(self):
        for vertex in self.vertices:
            print(vertex, ":", self.adj_list[vertex])


def topological_sort(diGraph):
    # construct a dictionary mapping nodes to their in-degree
    indegree = {node: 0 for node in diGraph.adj_list}
    for node in diGraph.adj_list:
        for neighbor in diGraph.adj_list[node]:
            indegree[neighbor] += 1

    print(f'In-degree of each nodes as node:in-degree -> {indegree}')

    node_with_indegree_zero = []  # A list to store all the nodes with in-degree zero
    for node in diGraph.adj_list:
        if indegree[node] == 0:
            node_with_indegree_zero.append(node)

    topological_ordering = []  # A list to store the final top sort order

    # as long as there are nodes with no incoming edges
    # that can be added to the ordering

    while len(node_with_indegree_zero) > 0:
        node_with_indegree_zero.sort()  # Sorting the list to pop as alphabetical order
        node = node_with_indegree_zero.pop(0)  # popping from left
        topological_ordering.append(node)  # add one of those nodes to the ordering

        for neighbor in diGraph.adj_list[node]:
            indegree[neighbor] -= 1  # decrement the in-degree of that node's neighbors
            if indegree[neighbor] == 0:
                node_with_indegree_zero.append(neighbor)

    # we've run out of nodes with no incoming edges
    # did we add all the nodes or find a cycle?
    
    if len(topological_ordering) == len(diGraph.adj_list):
        return topological_ordering
    else:
        raise Exception("Graph has a cycle! No topological ordering exists.")


"""
graph = {'A': ['B', 'C', 'D'],
         'B': ['A', 'E', 'D'],
         'C': ['A', 'D'],
         'D': ['A', 'B', 'C', 'E'],
         'E': ['B', 'D']
         }
"""
if __name__ == "__main__":
    number_of_nodes = int(input("Enter How many nodes? "))

    while True:
        nodes = list(map(str, input("Enter space separated nodes: ").strip().split()))
        if len(nodes) != number_of_nodes:
            print("number of nodes mismatched. Try again ")
        else:
            break

    graph = Graph(nodes, is_directed=True)
    # print(nodes)

    for node in nodes:
        neighbor_list = list(map(str, input(f"Enter space separated neighbors for node {node}: ").strip().split()))
        for neighbor in neighbor_list:
            graph.add_edge(node, neighbor)

    print(f'Adjacency list is :')
    graph.print_adj_list()

    topSort = topological_sort(graph)
    print(f'Topological Sort order is: {topSort}')
