from collections import defaultdict

class UndirectedGraph:

    def __init__(self) -> None:
        self.graph = defaultdict(list)

    def add_edge(self, u, v) -> None:
        self.graph[u].append(v)
        self.graph[v].append(u)


