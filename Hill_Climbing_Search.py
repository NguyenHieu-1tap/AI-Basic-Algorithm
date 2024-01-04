
data = []
graph = {}
length_lst = []
lst_length = []
listL1 = []
listL = []


def hill_climbing(x, start, end):
    y = str()
    explored = []
    path = []
    current_list = [start, ]

    with open(x + '.txt', "r") as fileIn:
        for i in fileIn:
            line, length, *lines = i.split()
            graph[line] = lines
            length_lst.append([length, line])
            # zippedGraph = zip(node_graph.items(), length_lst)

    while True:
        if len(current_list) == 0:
            raise Exception("No way Exception")

        current_node = current_list.pop(0)
        explored.append(current_node)
        # Check if node is goal-node
        if current_node == end:
            explored.append(end)
            return
        adjacent = graph[current_node]

        for b, c in length_lst:
            for a in adjacent:
                if c == a:
                    lst_length.append(int(b))
                if c == end:
                    break
        lst_length.sort()

        for a in lst_length:
            for b, c in length_lst:
                if a == int(b):
                    listL1.append(c)

        for i in reversed(listL1):
            listL.insert(0, i)
        y += str(current_node) + '\t' + str(adjacent) + '\t' + str(listL1) + '\t'
        listL1.clear()
        lst_length.clear()
        for node in reversed(listL):
            if node not in explored:
                current_list.insert(0, node)
            if current_node in listL:
                listL.remove(current_node)
        y += str(listL) + '\n'

        with open('Hill_Climbing_op.txt', 'w') as f:
            f.write(y)
            f.write(end)
            f.write('\n')
            f.write(str(list(explored)))




if __name__ == "__main__":
    print(hill_climbing("Hill_Climbing_ip", 'A', 'B'))
