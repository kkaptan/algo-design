"""
reverse linked list
"""

class Node:
    """node class"""
    def __init__(self, val, nxt = None):
        self.val = val
        self.nxt = nxt


def create_node_list(lst : list[int]) -> Node:
    """create a node list from a list of integers
    lst
    """
    cur = None
    prev = None

    i = len(lst) - 1

    if i == 0:
        return Node(lst[0])

    while (i >= 0): 
        cur = Node(lst[i], prev)
        prev = cur
        i = i - 1

    return cur

def traverse(node: Node) -> None:
    """traverses the linked list and prints the values"""
    while (node):
        print(node.val)
        node = node.nxt


def reverse_list(node):
    """reverses the single linked list"""
    prev = None
    cur = node
    while (cur):
        tmp = cur.nxt
        cur.nxt = prev
        prev = cur 
        cur = tmp

    return prev
        

def main():
    """main function reads the input of the testcases form standard
    input in the form:
    t - test cases
    n - number of integers in list
    1...n - integers in the list
    """
    rv = []
    n = int(input().strip())
    for i in range(n):
        rv.append(int(input().strip()))
    
    cur = create_node_list(rv)
    traverse(reverse_list(cur))

if __name__ == '__main__':
    main()
