class Node:

    def __init__(self, val, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors else []


def create_nodes(val, nodes, dct):
    """create nodes from a given list
    the value of the node is the index of the list + 1.
    
    For example, a node is represented as [[2,3]], where
    the value of the node is 1, since the index is 0 and the 
    neighbors of the node is 2 and 3.
    """
    if val in dct:
        node = dct[val]
    else:
        node = Node(val)
        dct[val] = node

    for n in nodes:
        if n in dct:
            node.neighbors.append(dct[n])
        else:
            new = Node(n)
            node.neighbors.append(new)
            dct[n] = new 

    return node 


def build_graph(lst):
    dct = {}
    for i, v in enumerate(lst):
        create_nodes(i+1, v, dct)
    if 1 in dct:
        return dct[1]

    return None


def traverse(g, visited):
    if g.val in visited:
        return

    print(g.val)
    visited.add(g.val)
    for i in g.neighbors:
        traverse(i, visited)

if __name__ == '__main__':
    first = build_graph([[2,3],[1, 3,4]])
    visited = set()
    traverse(first, visited)

