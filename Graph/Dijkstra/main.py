from graph import Graph


class Dijkstra:
    def min_district_index(self):
        # Get the index of vertex with minimum weight in that district
        min_value = float("inf")
        min_index = -1
        for i in self.range_list:
            if not self.is_vertex_set[i] and self.mdist[i] < min_value:
                min_index = i
                min_value = self.mdist[i]
        return min_index

    def __init__(self, graph: Graph, src, dest):
        self.src = src
        self.dest = dest
        self.graph = graph
        self.vertex_count = graph.vertex_count
        self.range_list = range(self.vertex_count)

        self.parent_list = [src for _ in self.range_list]  # A list of vertexes that  indicates which parent is the best choice for the shortest path.
        self.mdist = [float("inf") for _ in self.range_list]
        self.is_vertex_set = [False for _ in self.range_list]  # A list of booleans indicates whether the vertex is set or not.

        self.mdist[src] = 0.0
        self.parent_list[src] = -1

    def find_fastest_path(self):
        for _ in range(self.vertex_count - 1):
            u = self.min_district_index()
            self.is_vertex_set[u] = True

            for v in self.range_list:
                weight_u_to_v = self.graph.get_weight(u, v)
                if (
                        (not self.is_vertex_set[v])
                        and weight_u_to_v != float("inf")
                        and self.mdist[u] + weight_u_to_v < self.mdist[v]
                ):
                    self.parent_list[v] = u
                    self.mdist[v] = self.mdist[u] + weight_u_to_v

    def print_fastest_path(self):
        temp = self.dest
        print(self.dest, end="")
        while True:
            print(" <- ", end="")
            temp = self.parent_list[temp]
            print(temp, end="")
            if temp == self.src:
                break


if __name__ == "__main__":
    graph = Graph(vertex_count=5)
    graph.add_edge(src=0, dest=4, weight=10)
    graph.add_edge(src=0, dest=3, weight=100)
    graph.add_edge(src=0, dest=2, weight=30)
    graph.add_edge(src=0, dest=1, weight=50)
    graph.add_edge(src=2, dest=1, weight=5)
    graph.add_edge(src=3, dest=1, weight=20)
    graph.add_edge(src=3, dest=2, weight=50)
    graph.add_edge(src=4, dest=3, weight=10)

    dij = Dijkstra(graph, src=0, dest=1)
    dij.find_fastest_path()
    dij.print_fastest_path()
