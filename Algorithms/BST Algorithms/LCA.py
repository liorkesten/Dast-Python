def LCA(self, x, y):
    """
    Gets 2 nodes in the tree and return the LCA of them.
                Time Complexity O(n) - n is num of the nodes
    :param x: node in the tree
    :param y: node in the tree
    :return:
    """
    cur = x
    ancestor = x
    pass_ancestor = False
    while cur is not (y):
        if cur.right_child:
            cur = self.find_min(cur.right)
        else:
            while True:
                # If cur is right child - continune claiming
                if cur == cur.parent.right_child:
                    if cur == ancestor:
                        # if pass ancestor - we will have to update it.
                        pass_ancestor = True
                    cur = cur.parent
                    continue
                # if we claimed from left child.
                elif cur == cur.parent.left_child:
                    if pass_ancestor:  # Update ancestor
                        ancestor = cur
                        pass_ancestor = False  # reset pass_ ancestor
                    continue
                else:  # We are in the root of the tree
                    return self.LCA(y, x)  # Switch them
    return ancestor


def LCA_Dist(self, x, y):
    """
    Gets 2 nodes in the tree and return the LCA of them.
                Time Complexity O(k) - k is distance between x and y.
    :param x: node in the tree
    :param y: node in the tree
    :return:
    """
    cur_x = x
    cur_y = y
    steps_x, steps_y, step = 0, 0, 1
    found = False

    # Step 1: Find some Common ancestor.
    while True:
        #  Claim with cur_x
        for i in range(step):
            if cur_x is None:
                break
            cur_x = cur_x.parent
            steps_x += 1
            if cur_x == cur_y:
                found = True
        step *= 2
        if found:
            break
        #  Claim with cur_y
        for i in range(step):
            if cur_y is None:
                break
            cur_y = cur_y.parent
            steps_y += 1
            if cur_y == cur_x:
                found = True
        step *= 2
        if found: break

    # Step 2 : Equal the depth of cur_x and cur_y to CA (from Step 1)
    cur_x = x, cur_y = y
    if steps_y > steps_x:
        for i in range(steps_y - steps_x):
            cur_x = cur_x.parent
    elif steps_x > steps_y:
        for i in range(steps_x - steps_y):
            cur_y = cur_y.parent
    # Step 3: Claim with cur_x and cur_y together until they meet in the
    # LCA
    while True:
        if cur_x == cur_y:
            return cur_x  # same as return cur_y
        else:
            cur_x = cur_x.parent
            cur_y = cur_y.parent