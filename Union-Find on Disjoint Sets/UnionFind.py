class DisjointSet:
    parent = {}
    rank = {}

    def make_set(self, node):
        self.parent[node] = node
        self.rank[node] = 0

    def make_set_tree(self, node, parent, rank):
        self.parent[node] = parent
        self.rank[node] = rank

    def find_set(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find_set(self.parent[x])
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

    def print_paren_rank(self):
        parent_set = set(self.parent.values())
        child_dict = {}
        for parent in parent_set:
            child_dict[parent] = []

        for parent, child in self.parent.items():
            if child in parent_set:
                child_dict[child].extend(parent)

        print(f"Disjoint sets are : {child_dict}")
        #
        # print(f"Parent list {self.parent}")
        # print(self.rank)


if __name__ == "__main__":
    ds = DisjointSet()

    set_type = input("S for Singleton set | T for Undirected Tree : ").lower()
    number_of_nodes = int(input("Enter How many nodes? "))

    while True:
        if set_type == 's':
            nodes = list(map(str, input("Enter space separated nodes: ").strip().split()))
            if len(nodes) != number_of_nodes:
                print("number of nodes mismatched. Try again ")
            else:
                for node in nodes:
                    ds.make_set(node)
                break
        elif set_type == 't':
            for i in range(number_of_nodes):
                nodes = list(map(str, input("Enter space separated node, it's  parents, it's rank: ").strip().split()))
                ds.make_set_tree(nodes[0], nodes[1], nodes[2])
            break

    # print(ds.parent)
    number_of_union = int(input("Enter How many union operations? "))
    for i in range(number_of_union):
        X, Y = list(map(str, input("Enter space separated 1st node and 2nd Node to be united: ").strip().split()))
        ds.union(X, Y)

    ds.print_paren_rank()

# ds = DisjointSet()
# ds.make_set("c")
# ds.make_set("h")
# ds.make_set("e")
# ds.make_set("f")
# ds.make_set("d")
#
# ds.union("c", "h")
# ds.union("c", "e")
# ds.union("f", "d")
#
# ds.print_paren_rank()
