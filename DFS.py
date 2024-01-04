import ast


def dfs_path(graph, start, end):
    result = []
    dfs1(graph, start, end, [], result)
    b = str(result)
    with open('op.txt', 'a') as f:
        f.write('Shortest path DFS:\n')
        f.write(b)
    return result


def dfs1(graph, start, end, path, result):
    path += [start]
    if start == end:
        result.append(path)
    else:
        for node in graph[start]:
            if node not in path:
                dfs1(graph, node, end, path[:], result)

def dfs(graph, start, end):
    a = str()

    frontier = [start, ]
    explored = []

    while True:
        if len(frontier) == 0:
            raise Exception("No way Exception")
        current_node = frontier.pop()
        explored.append(current_node)
        neighbours = graph[current_node]

        # Check if node is goal-node
        if current_node == end:
            return

        # expanding nodes
        for node in reversed(graph[current_node]):

            if node not in explored:
                frontier.append(node)

        a += str(current_node) + '\t' + str(neighbours) + '\t' + str(frontier) + '\t' + '\n'

        with open('op.txt', 'w') as f:
            f.write(a)
            f.write('\n')


if __name__ == "__main__":
    # This is Tree
    with open('ip.txt') as f:
        data = f.read()
    # Graph using dictionary structure from a file
    graph = ast.literal_eval(data)

    print(dfs(graph, 'A', 'H'))
    print(dfs_path(graph, 'A', 'H'))
