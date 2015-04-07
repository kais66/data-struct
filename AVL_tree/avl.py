class AVLTreeNode:
    def __init__(self, x):
        self.val = x
        self.height = 0 # regular Bin Tree doesn't have this
        self.left = None
        self.right = None

    def getHeight(self, root):
        if root is None:
            return 0
        else:
            return root.height
    def getBalanceFactor(self. root):
        return self.getHeight(root.left) - self.getHeight(root.right)

    def insert(self, root, node):
        ''' using recursive bottom-up approach ''' 
        if root is None:
            self.root = node
        elif node.val < root.val:
            self.insert(root.left, node)
        else:
            self.insert(root.right, node)

        if self.getBalanceFactor(root) > 1: # root is un-balanced and left heavy
            lfac = self.getBalanceFactor(root.left)
            if lfac < 0: # left subtree is right heavy, regardless of whether lfac < -1 or not
                self.leftRotate(root.left)
            self.rightRotate(root)
        elif self.getBalanceFactor(root) < -1:
            rfac = self.getBalanceFactor(root.right)
            if rfac > 0: 
                self.rightRotate(root.right)
            self.leftRotate(root)

        root.height = max(self.getHeight(root.left), self.getHeight(root.right)) + 1

