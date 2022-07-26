from linked_list import LinkedList


class Graph:
    def __init__(self, vertex_count):
        self.vertex_count = vertex_count
        self.adj_list = [LinkedList(None, empty=True) for _ in range(vertex_count)]

    def get_weight(self, src, dest):
        if src == dest:
            return 0
        result = self.adj_list[src].get_weight_by_destination(dest)
        if result is None:
            raise ValueError(f"Invalid destination value for this vertex. {src} => {dest}")
        return result

    def add_edge(self, src: int, dest: int, weight: int):
        self.adj_list[src].append(value=(dest, weight))
