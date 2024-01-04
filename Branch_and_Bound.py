graph = {}
length_lst = []
k_lst = []
h_lst = []
g_lst = []
f_lst = []
listL1 = []
listL = []
current_list = []
lst_node = []
lst_length = []


def bab(x, start, end):
    y = str()
    explored = []
    path = []
    #current_list = [start, ]
    current_node = start
    current_length = 0

    # File input
    with open(x + '.txt', 'r') as f:
        for i in f:
            node, h, *line = i.split()
            graph[node] = line
            length_lst.append((h, node))

    # Init graph
    for a, b in graph.items():
        for c in b:
            if c.isalpha():
                lst_node.append(c)
            if c.isnumeric():
                lst_length.append(c)
        graph[a] = list(zip(lst_length, lst_node))

        lst_node.clear()
        lst_length.clear()
    for a, b in graph.items():
        if len(b) == 0:
            b.append('No adjacent !!!')

    # Algorithm
    while True:
        #if len(current_list) == 0:
         #   raise Exception('No way Exception')

        #current_node = listL.pop(0)
        if len(listL) != 0:
            listL.pop(0)

        if current_node == end:
            explored.append(end)
            return

        adjacent = graph[current_node]
        g = 0
        # Init g_lst
        if adjacent[0] == 'No adjacent !!!':
            continue
        for x, y in adjacent:
            g_lst.append(int(x) + g)
        g = min(g_lst)

        # Init h_lst
        for a, b in adjacent:
            for c, d in length_lst:
                if b == d:
                    h_lst.append(int(c))

        # Init f_lst
        for i in range(0, len(g_lst)):
            f_lst.append(g_lst[i] + h_lst[i])

        # Init listL1
        for x, y in adjacent:
            lst_length.append(y)
        listL1 = list(zip(f_lst, lst_length))
        listL1.sort()

        # Init listL
        for i in reversed(listL1):
            listL.insert(0, i)

        print(g_lst)
        print(h_lst)
        print(f_lst)
        print(listL1)
        print(listL)

        # Init recursion
        g_lst.clear()
        h_lst.clear()
        f_lst.clear()
        current_list.clear()
        for x, y in listL:
            current_list.insert(-1, y)
        print(current_list)

        explored.append(current_node)
        for x, y in listL:
            if current_node == y:
                current_length = x
                break
        print(explored)
        print(current_length)


if __name__ == '__main__':
    bab('BaB_ip', 'A', 'B')
