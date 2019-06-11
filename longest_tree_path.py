"""
Write a function that computes the length of the longest path of consecutive integers in a tree.

A node in the tree has a value and a set of children nodes.
A tree has no cycles and each node has exactly one parent.
A path where each node has a value 1 greater than its parent is a path of consecutive integers
(e.g. 1,2,3 not 1,3,5).

A few things to clarify:
Integers are all positive
Integers appear only once in the tree

Test Cases
Note that there may be other valid answers.
"""


class Node:
    def __init__(self, val, children=None):

        if val < 0:
            raise ValueError("Value cannot be negative")

        self.val = val  # positive integer
        self.children = children  # list of children nodes


def longest_tree_path(root, parent_val=-1, cur_len=None, maxlen=None):

    # root node does not exist
    if root is None:
        return maxlen

    # root node is the first node of the tree
    if parent_val == -1:
        cur_len = 1
        maxlen = 1

    # consecutive nodes found
    elif root.val == parent_val + 1:
        cur_len += 1
        if cur_len > maxlen:
            maxlen = cur_len

    if root.children is not None:
        # check maxlen for all the children of the current node
        for node in root.children:
            # recurse all the way!
            child_len = longest_tree_path(node, root.val, cur_len, maxlen)
            if child_len > maxlen:
                maxlen = child_len

    return maxlen


if __name__ == '__main__':

    # tree1: provided case
    four = Node(4, None)
    two = Node(2, [four])
    three = Node(3, None)
    one = Node(1, [two, three])

    assert(longest_tree_path(one) == 2)

    # tree2: provided case
    fifteen = Node(15, None)
    ten = Node(10, None)
    nine = Node(9, [fifteen, ten])
    eight = Node(8, [nine])
    twelve = Node(12, None)
    seven = Node(7, [eight, twelve])
    six = Node(6, None)
    five = Node(5, [six, seven])

    assert(longest_tree_path(five) == 4)

    # additional test cases
    # tree4: no tree
    assert (longest_tree_path(None) == None)

    # tree3: single node
    root = Node(1, None)
    assert(longest_tree_path(root) == 1)

    # tree4:
    five = Node(5, None)
    three = Node(3, [five])
    seven = Node(7, None)
    nine = Node(9, None)
    one = Node(1, [seven, nine])
    two = Node(2, [three, one])

    assert(longest_tree_path(two) == 2)

    # tree5
    seven = Node(7, None)
    eight = Node(8, None)
    six = Node(6, [seven, eight])
    one = Node(1, [six])
    five = Node(5, None)
    four = Node(4, None)
    three = Node(3, [five, four])
    two = Node(2, [one, three])

    assert(longest_tree_path(two) == 3)


    # tree6
    three = Node(3, None)
    five = Node(5, None)
    seven = Node(7, None)
    one = Node(1, [three, five, seven])

    assert(longest_tree_path(one) == 1)

    # tree7
    four = Node(4, None)
    three = Node(3, [four])
    five = Node(5, None)
    eight = Node(8, None)
    seven = Node(7, [eight])
    one = Node(1, [three, five, seven])

    assert(longest_tree_path(one) == 2)

    # tree8
    five = Node(5, None)
    four = Node(4, [five])
    three = Node(3, [four])
    six = Node(6, None)
    eight = Node(8, None)
    seven = Node(7, [eight])
    one = Node(1, [three, five, seven])

    assert (longest_tree_path(one) == 3)