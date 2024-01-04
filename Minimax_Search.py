import math


class Node:
    def __init__(self, name, value, child):
        self.name = name
        self.value = value
        self.child = child


def check_node(ip, lst_node):
    for i in lst_node:
        if i.name == ip:
            return i


def check_leaf_node(Node):
    if not Node.child:
        Node.child = 'Leaf Node'
        return True


def max_value(Node):
    if check_leaf_node(Node):
        return Node.value
    Node.value = -math.inf
    for child in Node.child:
        Node.value = max(Node.value, min_value(check_node(child, lst_node)))
    return Node.value


def min_value(Node):
    if check_leaf_node(Node):
        return Node.value
    Node.value = math.inf
    for child in Node.child:
        Node.value = min(Node.value, max_value(check_node(child, lst_node)))
    Node.value = Node.value
    return Node.value


def minimax(Node, state):
    if state == 'MAX':
        Node.value = max_value(Node)
    else:
        Node.value = min_value(Node)


if __name__ == '__main__':

    lst_node = []

    with open("Minimax_ip.txt", "r") as f:

        state = next(f).rstrip('\n')
        for i in f:
            name, value, *child = i.split()
            value = int(value)
            aNode = Node(name, value, child)
            lst_node.append(aNode)

    minimax(lst_node[0], state)

    output = ''
    for node in lst_node:
        output += node.name + '(' + str(node.value) + ')' + ': ' + str(node.child) + '\n'
    with open("Minimax_op.txt", "w") as f:
        f.write(output)
        f.close