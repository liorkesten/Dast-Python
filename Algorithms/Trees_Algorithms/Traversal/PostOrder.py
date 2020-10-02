from Algorithms.Trees_Algorithms.Traversal.NodeForTraversal import Node


def post_order_tree_recursive(f, node: "Node") -> None:
    """
    :param f: Function on each node
    :param node: root of tree
    :return: None
    """

    if node:
        post_order_tree_recursive(f, node.left)
        post_order_tree_recursive(f, node.right)
        f(node)


def post_order_tree_iter(f, root: "Node") -> None:
    """
    :param f: Function on each node
    :param root: root of tree
    :return: None
    """
    stack = []
    while root or stack:
        # Step 1: Add nodes in the following order: right-> node -> left
        while root:
            if root.right:
                stack.append(root.right)
            stack.append(root)
            root = root.left

        root = stack.pop()
        # Step 2: go to right subtree:
        if stack and stack[-1] == root.right:
            # Swap the root and the its right child:
            stack[-1], root = root, stack[-1]
        else:
            f(root)
            root = None
