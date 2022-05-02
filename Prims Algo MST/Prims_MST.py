"""A python program that find Minimum Spanning Tree (MST) using Prim's Algo with the help of Priority Queue
Operations """
import queue


class Graph:
    def __init__(self, vertices, is_directed=False):
        self.vertices = vertices
        self.adj_list = {}
        self.is_directed = is_directed

        for vertex in self.vertices:
            self.adj_list[vertex] = {}

    def add_edge(self, source, destination, weight):
        self.adj_list[source][destination] = weight
        if not self.is_directed:
            self.adj_list[destination][source] = weight

    def print_adj_list(self):
        for vertex in self.vertices:
            print(vertex, ":", self.adj_list[vertex])


def prim(graph):
    pq = queue.PriorityQueue()
    mst = []
    visited = set()

    starting_vertex = list(graph.keys())[0]  # choosing the first vertex as the MST starting node

    # adding the adjacency info of the starting node
    for adj_node, cost in graph[starting_vertex].items():
        if adj_node not in visited:
            pq.put((cost, starting_vertex, adj_node))

    while pq.empty() is False:
        edge = pq.get()
        cost, src, dest = edge

        if dest in visited:
            continue

        visited.add(src)
        visited.add(dest)
        mst.append(edge)

        for adj_node, cost in graph[dest].items():
            if adj_node not in visited:
                pq.put((cost, dest, adj_node))

    return mst


def print_mst(mst):
    mst_cost = 0
    for edge in mst:
        # mst is a list of tuples as : [(cost, source, destination)]
        print(f'{edge[1]} <---> {edge[2]} :: {edge[0]}')
        mst_cost += edge[0]
    print(f"Total MST cost : {mst_cost}")


if __name__ == "__main__":
    number_of_nodes = int(input("Enter How many nodes? "))
    # graph_type = input("D for Directed Graph | U for Undirected Graph : ").lower()

    while True:
        nodes = list(map(str, input("Enter space separated nodes: ").strip().split()))
        if len(nodes) != number_of_nodes:
            print("number of nodes mismatched. Try again ")
        else:
            break

    # if graph_type == 'd':  # for 'directed' graph
    #     graph = Graph(nodes, is_directed=True)
    # else:
    #     graph = Graph(nodes, is_directed=False)
    # # print(nodes)

    graph = Graph(nodes, is_directed=False)

    print(f"Enter space separated neighbors and their edge weights. Split multiple neighbors by comma:")
    for node in nodes:
        neighbor_list = list(map(str, input(f"For node '{node}' : ").strip().split(',')))
        # print(neighbor_list)
        for neighbor in neighbor_list:
            adjacent_node, weight = neighbor.strip().split()
            # print(adjacent_node, weight)
            graph.add_edge(node, adjacent_node, int(weight))

    # print(f'Adjacency list is :')
    # graph.print_adj_list()

    min_span_tree = prim(graph.adj_list)

    print_mst(min_span_tree)
