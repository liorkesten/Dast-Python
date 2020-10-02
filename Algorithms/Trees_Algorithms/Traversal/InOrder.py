from Algorithms.Trees_Algorithms.Traversal.NodeForTraversal import Node


def in_order_tree_recursive(f, node: "Node") -> None:
    """
    :param f: Function on each node
    :param node: root of tree
    :return: None
    """

    if node:
        in_order_tree_recursive(f, node.left)
        f(node)
        in_order_tree_recursive(f, node.right)


def in_order_tree_iter(f, root: "Node") -> None:
    """
    Traversal Without using parent pointer - iterative.
    :param f: Function on each node
    :param root: root of tree
    :return: None
    """
    stack = []
    cur = root
    while True:
        # Add all left children
        if cur is not None:
            stack.append(cur)
            cur = cur.left
        elif cur:
            cur = cur.pop()
            f(cur)
            cur = cur.right  # check the right subtree
        else:
            break
