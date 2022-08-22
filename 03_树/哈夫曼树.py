class TreeNode(object):
    def __init__(self, weight, name=None):
        self.name = name
        self.weight = weight
        self.left = None
        self.right = None
        self.parent = None

    def isLeftChild(self):
        return self.parent.left == self

class HFtree(object):
    def __init__(self, frequency:dict):
        self.leaves = []
        self.root = None
        self.HFcodes = {}
        self.createLeaves(frequency)
        self.createHFtree(self.leaves.copy())

    def createLeaves(self, frequency:dict):
        for name in frequency.keys():
            self.leaves.append(TreeNode(frequency[name], name))
    
    def createHFtree(self, nodes:list):
        n = len(nodes)
        for _ in range(n-1):
            nodes.sort(key=lambda node:node.weight, reverse=True)
            left:TreeNode = nodes.pop()
            right:TreeNode = nodes.pop()
            newNode = TreeNode(left.weight+right.weight)
            newNode.left = left
            newNode.right = right
            left.parent = newNode
            right.parent = newNode
            nodes.append(newNode)
        self.root = nodes[0]

    def createHFcodes(self):
        for leaf in self.leaves:
            code = ""
            name = leaf.name
            while leaf.parent is not None:
                if leaf.isLeftChild():
                    code = '0' + code
                else:
                    code = '1' + code
                leaf = leaf.parent
            self.HFcodes[name] = code

a = {'a': 9, 'b': 12, 'c': 6, 'd': 3, 'e': 5, 'f': 15}
b = {'a': 3, 'b': 2, 'c': 3}
myHFtree = HFtree(a)
myHFtree.createHFcodes()
print(myHFtree.HFcodes)