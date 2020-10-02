from Algorithms.Trees_Algorithms.Traversal.NodeForTraversal import Node


def pre_order_tree_recursive(f, node: "Node") -> None:
    """
    node -> Left -> Right
    :param f: Function on each node
    :param node: root of tree
    :return: None
    """

    if node:
        f(node)
        pre_order_tree_recursive(f, node.left)
        pre_order_tree_recursive(f, node.right)


def pre_order_tree_iter(f, root: "Node") -> None:
    """
    :param f: Function on each node
    :param root: root of tree
    :return: None
    """
    stack = [root]
    while stack:
        cur = stack.pop()
        if cur:  # Check that cur is not None
            f(cur)
            # add first stack and than left - left should be popped first
            stack.append(cur.right)
            stack.append(cur.left)


if __name__ == '__main__':
    a = Node(5, Node(3, Node(2, None, Node(2.5)),
                     Node(4, Node(3.5, Node(3.2), Node(3.7)))), Node(6))
    pre_order_tree_recursive(print, a)
    print("-----")
    pre_order_tree_iter(print, a)
