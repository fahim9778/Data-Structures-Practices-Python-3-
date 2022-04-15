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


def dfs_iterative(root_node, graph):
    """ A function that solves Depth First Search in the Iterative Approach using stack """
    visited = set()  # to see if the current node is already visited or not
    if root_node not in graph.adj_list:
        print("Start Node couldn't be found. Program is existing...")
        return

    stack = [root_node]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(f'{vertex} -> ', end='')
            visited.add(vertex)
            for adjacent_node in graph.adj_list[vertex]:
                if adjacent_node not in visited:
                    stack.append(adjacent_node)
    print('Stop.')


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
    graph_type = input("D for Directed Graph | U for Undirected Graph : ").lower()

    while True:
        nodes = list(map(str, input("Enter space separated nodes: ").strip().split()))
        if len(nodes) != number_of_nodes:
            print("number of nodes mismatched. Try again ")
        else:
            break

    if graph_type == 'd':  # for 'directed' graph
        graph = Graph(nodes, is_directed=True)
    else:
        graph = Graph(nodes, is_directed=False)
    # print(nodes)

    for node in nodes:
        neighbor_list = list(map(str, input(f"Enter space separated neighbors for node {node}: ").strip().split()))
        for neighbor in neighbor_list:
            graph.add_edge(node, neighbor)

    print(f'Adjacency list is :')
    graph.print_adj_list()

    start_node = input("Enter root node to start DFS: ")
    dfs_iterative(start_node, graph)
