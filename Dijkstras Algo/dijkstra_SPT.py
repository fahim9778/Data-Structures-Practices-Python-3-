"""A python program that find The Shortest Path Tree (SPT) using Dijkstra's Algo with the help of Priority Queue
Algorithm """
import heapq


class Graph:
    def __init__(self, vertices, is_directed=True):
        self.vertices = vertices
        self.adj_list = {}
        self.is_directed = is_directed

        for vertex in self.vertices:
            self.adj_list[vertex] = {}

    def add_edge(self, source, destination, weight):
        self.adj_list[source][destination] = weight
        # if not self.is_directed:
        #     self.adj_list[destination][source] = weight

    def print_adj_list(self):
        for vertex in self.vertices:
            print(vertex, ":", self.adj_list[vertex])


def dijkstra(graph, starting_node):
    if starting_node not in graph:
        raise Exception("Invalid Starting Node.")

    visited = set()
    parent_dict = {}
    pq = []
    distances = {vertex: float('infinity') for vertex in graph}

    distances[starting_node] = 0
    parent_dict[starting_node] = None
    heapq.heappush(pq, (0, starting_node))

    while pq:
        current_dist, current_node = heapq.heappop(pq)
        visited.add(current_node)

        for adj_node, weight in graph[current_node].items():
            if adj_node in visited:
                continue

            new_dist = current_dist + weight

            if new_dist < distances[adj_node]:
                parent_dict[adj_node] = current_node
                distances[adj_node] = new_dist
                heapq.heappush(pq, (new_dist, adj_node))

    return parent_dict, distances


def spt_path(parent_dict, goal):
    if goal not in parent_dict:
        return None
    v = goal
    path = []
    while v is not None:  # until we reach the root node
        path.append(v)  # append this node to the list
        v = parent_dict[v]  # search for it's parent, recursively.
    return path[::-1]  # once done, return a reversed list


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

    graph = Graph(nodes, is_directed=True)

    print(f"Enter space separated neighbors and their edge weights. Split multiple neighbors by comma:")
    for node in nodes:
        neighbor_list = list(map(str, input(f"For node '{node}' : ").strip().split(',')))
        for neighbor in neighbor_list:
            # check if the input is empty
            if '' in neighbor_list:
                adjacent_node, weight = None, None
            else:
                adjacent_node, weight = neighbor.strip().split()
                # print(adjacent_node, weight)
                graph.add_edge(node, adjacent_node, int(weight))
        print(graph.adj_list)

    print(f'Adjacency list is :')
    graph.print_adj_list()

    # parent, SPT_dist = dijkstra(graph.adj_list, 'A')
    # print(parent, SPT_dist)
    # for node in graph.adj_list:
    #     print(spt_path(parent, node))

    start_node = input(f"Enter Starting Node: ").strip()
    parent, SPT_dist = dijkstra(graph.adj_list, start_node)

    for node, distance in SPT_dist.items():
        print(f"{start_node} --> {node} distance is {distance} and path {spt_path(parent, node)}")
