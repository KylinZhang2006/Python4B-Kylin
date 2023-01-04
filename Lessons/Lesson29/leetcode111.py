class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
t15 = TreeNode(15)
t7 = TreeNode(7)
t20 = TreeNode(20,t15,t7)
t9 = TreeNode(9)
t3 = TreeNode(3,t9,t20)
def minDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0
    queue = []
    depth = 0
    queue.append(root)
    while queue:
        size = len(queue)
        depth += 1
        for i in range(size):
            node = queue.pop(0)
            if not node.left and not node.right:
                return depth
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
print(minDepth(t3))
