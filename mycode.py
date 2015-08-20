#https://archive.is/vyskg
# Create a function that prints the tree elements in order from left-most to right-most
# The tree structure has been flattened like this
#
# tree = []
# tree[0] = new Node('root', 1,  2)
# tree[1] = new Node('left',  /*<mightexist> */,  <mightexist>)
# tree[2] = new Node('right', None, None)
# .... more tree[*] entries
#
# the root of the tree will always be at index 0

class Node:
    def __init__ (self, value, left, right):
       self.value = value
       self.left = left
       self.right = right

???, "left", ???, "root", "right"

class BinaryTree:
    def __init__(self):
        pass

    def print_nodes_inorder(self, node):
        #if node == None: // right case
        #    print(node.parent) // can't be done
        traverse / print left
        print middle
        traverse / print right

        if node == None:
            print("")
            return None
        elif node.left == None:
            print(node.value)
            self.print_nodes_inorder(right)
        //elif node.right == None:
        //    print(node.value)
        else:
            self.print_nodes_inorder(left)
