class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.p = None
        # list of occurrences
        self.occList = []


class BinaryTree:
    def __init__(self):
        self.root = None
        self.currentI = -1

    def length(self):
        return self.size

    def inorder(self, node):
        if node is None:
            return None
        else:
            self.inorder(node.left)
            print(node.key)
            self.inorder(node.right)

    def search(self, k):
        node = self.root
        while node is not None:
            if node.key == k:
                return node
            if node.key > k:
                node = node.left
            else:
                node = node.right
        return None

    def minimum(self, node):
        x = None
        while node.left is not None:
            x = node.left
            node = node.left
        return x

    def maximum(self, node):
        x = None
        while node.right is not None:
            x = node.right
            node = node.right
        return x

    def getMax(self):
        return self.maximum(self.root).key
    def getMin(self):
        return self.minimum(self.root).key
    def getUp(self):
        return self.minimum(self.root).p.key

    def successor(self, node):
        parent = None
        if node.right is not None:
            return self.minimum(node.right)
        parent = node.p
        while parent is not None and node == parent.right:
            node = parent
            parent = parent.p
        return parent

    def predecessor(self, node):
        parent = None
        if node.left is not None:
            return self.maximum(node.left)
        parent = node.p
        while parent is not None and node == parent.left:
            node = parent
            parent = parent.p
        return parent

    def insert(self, k, i):
        self.currentI += 1
        t = TreeNode(k)
        parent = None
        node = self.root
        while node is not None:
            parent = node
            if node.key > t.key:
                node = node.left
            else:
                node = node.right
        t.p = parent
        if parent is None:
            t.occList.append(self.currentI)
            self.root = t
        elif t.key == parent.key:
            parent.occList.append(self.currentI)
        elif t.key < parent.key:
            parent.left = t
            parent.left.occList.append(self.currentI)
        else:
            parent.right = t
            parent.right.occList.append(self.currentI)
        return t

    def delete(self, node):
        if node.left is None:
            self.transplant(node, node.right)
        elif node.right is None:
            self.transplant(node, node.left)
        else:
            succ = self.minimum(node.right)
            if succ.p != node:
                self.transplant(succ, succ.right)
                succ.right = node.right
                succ.right.p = succ
            self.transplat(node, succ)
            succ.left = node.left
            succ.left.p = succ

    def searchByI(self, node, i):
        while loc == -1:
            if node.left is not None:
                searchByI(node.left)


        # while len(nodes)

    def deleteByI(self, k, i):
        node = self.search(k)
        node.occList.remove(i)

    def transplant(self, node, newnode):
        if node.p is None:
            self.root = newnode
        elif node == node.p.left:
            node.p.left = newnode
        else:
            node.p.right = newnode
        if newnode is not None:
            newnode.p = node.p


def simple_max(vals):
    return max(vals)

def run_blt(vals, k):
    blt = BinaryTree()
    for val in vals:
        blt.insert(val, 0)

if __name__ == "__main__":
    blt = BinaryTree()
    # blt.insert(3)
    # blt.insert(6)
    # blt.insert(2)
    # print(str(blt.maximum(0)))
    # print(str(blt.minimum(0)))
    blt.insert(3, 0)
    blt.insert(6, 1)
    blt.insert(2, 2)
    blt.insert(2, 3)
    blt.insert(2, 4)
    blt.insert(2, 5)
    print(str(blt.getMax()))
    print(str(blt.getMin()))
    print(str(blt.getUp()))

    _NUMBER = 1000

    from timeit import Timer

    import random
    vals = random.sample(range(10000), 10000)

    t0 = Timer(lambda: simple_max(vals))
    t1 = Timer(lambda: run_blt(vals, 8))

    print("{0} simple_max: {1}".format(_NUMBER, t0.timeit(number=_NUMBER)))
    print("{0} run_blt: {1}".format(_NUMBER, t1.timeit(number=_NUMBER)))
