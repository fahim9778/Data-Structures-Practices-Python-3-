"""A python program that find Minimum Spanning Tree (MST) using Kruskal's Algo with the help of Union-Find Operations"""


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append([u, v, weight])

    def sort_edges(self):
        self.edges = sorted(self.edges, key=lambda item: item[2])  # ascending order soring based on edge weight

    def get_edges(self):
        return self.edges

    def get_vertices(self):
        return self.vertices


class DisjointSet:
    def __init__(self, vertices):
        self.parent = {}
        self.rank = {}

        for node in vertices:
            self.parent[node] = node
            self.rank[node] = 0

    def find_set(self, x):
        if self.parent[x] != x:
            return self.find_set(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rep_of_x = self.find_set(x)
        rep_of_y = self.find_set(y)

        if rep_of_x != rep_of_y:
            if self.rank[rep_of_x] > self.rank[rep_of_y]:
                self.parent[rep_of_y] = rep_of_x
            elif self.rank[rep_of_y] > self.rank[rep_of_x]:
                self.parent[rep_of_x] = rep_of_y
            else:
                self.parent[rep_of_y] = rep_of_x
                self.rank[rep_of_x] += 1


def kruskal(graph):
    mst = []
    graph.sort_edges()
    disjoint_set = DisjointSet(graph.get_vertices())
    for (u, v, weight) in graph.get_edges():
        if disjoint_set.find_set(u) != disjoint_set.find_set(v):
            mst.append([u, v, weight])
            disjoint_set.union(u, v)
    return mst


def print_mst(mst):
    min_mst_cost = 0
    for line in range(len(mst)):
        print(f"{mst[line][0]} <-> {mst[line][1]} :: {mst[line][2]}")
        min_mst_cost += mst[line][2]
    print(f'Total Minimum Spanning Tree Cost = {min_mst_cost}')


if __name__ == "__main__":
    number_of_nodes = int(input("Enter How many nodes? "))
    while True:
        nodes = list(map(str, input("Enter space separated nodes: ").strip().split()))
        if len(nodes) != number_of_nodes:
            print("number of nodes mismatched. Try again ")
        else:
            break

    g = Graph(nodes)

    number_of_edges = int(input("Enter How many edges? "))

    while number_of_edges:
        src, dest, weight = list(
            map(str, input("Enter space separated 1st node, 2nd Node, Edge weight: ").strip().split()))
        g.add_edge(src, dest, int(weight))
        number_of_edges -= 1

    min_spanning_tree = kruskal(g)
    print_mst(min_spanning_tree)
