# Python implementation to find the shortest path in the graph using dictionaries

# Function to find the shortest path between two nodes of a graph
import ast


def BFS_SP(graph, start, goal):
    explored = []
    a = str()

    # the BFS traversal result
    bfs_traversal = list()

    # Queue for traversing the graph in the BFS
    queue = [[start]]

    # If the desired node is reached
    if start == goal:
        print("Same Node")
        return

    # Loop to traverse the graph with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1]
        bfs_traversal.append(node)

        a += str(node) + '\n'
        with open('test.txt', 'w') as f:
            f.write(a)

        print(node)

        # Condition to check if the current node is not visited
        if node not in explored:
            neighbours = graph[node]
            print(neighbours)

            # Loop to iterate over the neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                # Condition to check if the neighbour node is the goal
                if neighbour == goal:
                    with open('op.txt', 'w') as f:
                        f.writelines(str(bfs_traversal))
                        f.write("\n")
                        f.writelines(new_path)
                    f.close()

                    print("BFS: ", bfs_traversal)
                    print("Shortest path = ", *new_path)
                    return
            explored.append(node)

    # Condition when the nodes are not connected
    print("So sorry, but a connecting path doesn't exist :(")
    return


# Driver Code
if __name__ == "__main__":
    with open('ip.txt') as f:
        data = f.read()
    # Graph using dictionary structure from a file
    graph = ast.literal_eval(data)

    # Function Call
    BFS_SP(graph, 'A', 'H')
    f.close()
