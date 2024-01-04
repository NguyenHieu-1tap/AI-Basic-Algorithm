def bfs(graph, source, end):
    visited = set()  # to keep track of already visited nodes
    bfs_traversal = list()  # the BFS traversal result
    queue = list()  # queue

    # push the root node to the queue and mark it as visited
    queue.append(source)
    visited.add(source)

    # loop until the queue is empty
    while queue:
        # pop the front node of the queue and add it to bfs_traversal
        current_node = queue.pop(0)
        bfs_traversal.append(current_node)

        # check all the neighbour nodes of the current node
        for neighbour_node in graph[current_node]:
            # if the neighbour nodes are not already visited,
            # push them to the queue and mark them as visited
            if neighbour_node not in visited and neighbour_node != end:
                visited.add(neighbour_node)
                queue.append(neighbour_node)
            else:
                break

    return bfs_traversal


def main():
    graph = {
        'A': ['B', 'C', 'D'],
        'B': ['K'],
        'C': ['E'],
        'D': ['F', 'G'],
        'G': ['H'],
        'K': [],
        'E': [],
        'F': [],
        'H': []
    }

    with open('graph.txt', 'w') as f:
        bfs_traversal = bfs(graph, 'A', 'B')
        f.writelines(bfs_traversal)
        print(f"BFS: {bfs_traversal}")


if __name__ == '__main__':
    main()
