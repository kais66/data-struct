class TreeNode:
    def __init__(self, val, p=None):
        self.val = val
        self.parent = p 
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root):
        self.root = root

    def treeMinimum(self, root):
        ''' return the node with min value in the BST, or first node to visit inorder in general bin tree '''
        if root is None: return None
        while root.left is not None:
            root = root.left
        return root

    def treeMaximum(self, root):
        if root is None: return None
        while root.right is not None:
            root = root.right
        return root

    def successor(self, root):
        ''' assuming parent reference for every node, return root's in-order successor '''
        if not root: 
            raise AttributeError # if you want to find a successor, you have to provide a legit node
        if root.right is not None:
            return self.treeMinimum(root.right)

        p = root.parent
        while p is not None and p.right is root:
            root = p
            p = p.parent
        return p

    def predecessor(self, root):
        if not root:
            raise AttributeError
        if root.left is not None:
            return self.treeMaximum(root.left)

        p = root.parent
        while p is not None and p.left is root:
            root = p
            p = p.parent
        return p

    def insert(self, node): # this insertion does not guarantee balance of tree
        if self.root is None:
            self.root = node
            return
        x = self.root
        p = None
        while x is not None:
            p = x
            if node.val <= x.val:
                x = x.left
            else:
                x = x.right
        if node.val < p.val:
            p.left = node
        else:
            p.right = node

    def delete(self, node):
        ''' delete a node, given a reference to it. It uses the transplant() subroutine '''
        if node.left is None:
            self.__transplant(node, node.right)
        elif node.right is None:
            self.__transplant(node, node.left)
        else:
            y = self.treeMinimum(node.right)
            if y.parent is not node: # then need to place y.right at the right place, because y is to be removed
                self.__transplant(y, y.right) # replace y by y's right subtree
                y.right = node.right 
                y.right.parent = y
            self.__transplant(node, y) # replace node by its right subtree
            y.left = node.left
            y.left.parent = y

    # page 296, transplant(), 
    def __transplant(self, u, v):
        ''' it replaces the subtree rooted at u with the subtree rooted at v '''
        if u is None or u.parent is None: # if u.parent does not exist, then it means u used to be root
            self.root = v
        elif u.parent.left is u::
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None and u is not None:
            v.parent = u.parent



class AVLTree(Tree):
    def insert(self, root, node):
        super(AVLTree, self).insert(root, node)
        self.__updateBalance(node) 

    def __updateBalance(self, root):
        
