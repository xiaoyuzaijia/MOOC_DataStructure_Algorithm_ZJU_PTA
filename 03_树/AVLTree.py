class TreeNode():
    def __init__(self, data=None):
        self.data = data
        self.left:TreeNode = None
        self.right:TreeNode = None
        self.height = 0

class AVLTree():
    def __init__(self):
        self.root = None

    def getHeight(self, node:TreeNode):
        if node is None:
            return -1
        else:
            return node.height

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self.root = self._insert(self.root, data)

    def _insert(self, node:TreeNode, data) -> TreeNode:   # 将data插入node为根的树中,并返回插入后的树根
        if node is None:
            node = TreeNode(data)
        elif data < node.data:
            node.left = self._insert(node.left, data)
            if self.getHeight(node.left) - self.getHeight(node.right) == 2:
                if data < node.left.data:
                    node = self.llRotate(node)
                elif data > node.left.data:
                    node = self.lrRotate(node)
        elif data > node.data:
            node.right = self._insert(node.right, data)
            if self.getHeight(node.left) - self.getHeight(node.right) == -2:
                if data > node.right.data:
                    node = self.rrRotate(node)
                elif data < node.right.data:
                    node = self.rlRotate(node)
        # else 要插入的data已存在
        node.height = max(self.getHeight(node.left), self.getHeight(node.right)) + 1
        return node

    def llRotate(self, node:TreeNode) -> TreeNode:  # 将node为根的树旋转后,并返回新的根
        newRoot = node.left
        node.left = newRoot.right
        newRoot.right = node
        node.height = max(self.getHeight(node.left), self.getHeight(node.right)) + 1
        newRoot.height = max(self.getHeight(newRoot.left), self.getHeight(newRoot.right)) + 1
        return newRoot

    def rrRotate(self, node:TreeNode) -> TreeNode:
        newRoot = node.right
        node.right = newRoot.left
        newRoot.left = node
        node.height = max(self.getHeight(node.left), self.getHeight(node.right)) + 1
        newRoot.height = max(self.getHeight(newRoot.left), self.getHeight(newRoot.right)) + 1
        return newRoot

    def lrRotate(self, node:TreeNode) -> TreeNode:
        node.left = self.rrRotate(node.left)
        return self.llRotate(node)

    def rlRotate(self, node:TreeNode) -> TreeNode:
        node.right = self.llRotate(node.right)
        return self.rrRotate(node)
