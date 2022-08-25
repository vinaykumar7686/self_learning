from undirected_graph import UndirectedGraph


def traverse_dfs(graph, start, visited_flags):
    print(graph, start, visited_flags)
    stack = [start]
    visited_flags[start] = True

    response = []

    while stack:
        current = stack.pop(-1)
        response.append(current)
        neighbors = graph[current]

        for neighbor in neighbors:
            if not visited_flags[neighbor]:
                stack.append(neighbor)
                visited_flags[neighbor] = True
    
    return response

        



if __name__ == "__main__":
    graph_obj = UndirectedGraph()
    graph_obj.add_edge(0,1)
    graph_obj.add_edge(0,2)
    graph_obj.add_edge(3,1)
    graph_obj.add_edge(4,2)

    graph_obj.add_edge(5,6)
    graph_obj.add_edge(6,7)
    graph_obj.add_edge(7,5)
    graph_obj.add_edge(5,8)

    graph = graph_obj.graph

    total_vertices = len(graph)
    visited_flags = [False for _ in range(total_vertices)]
    
    responses = []
    while False in visited_flags:
        index = visited_flags.index(False)

        responses.append(
            traverse_dfs(graph=graph, start=list(graph.keys())[index], visited_flags=visited_flags)
            )

    print(responses)
