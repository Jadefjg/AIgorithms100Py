class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root):
    if root is None:
        return None

    # 递归地翻转左子树和右子树
    left = invert_tree(root.left)
    right = invert_tree(root.right)

    # 交换左右子树
    root.left = right
    root.right = left

    return root


# 创建一个示例二叉树
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

# 翻转二叉树
inverted_root = invert_tree(root)

# 打印翻转后的二叉树
# 这里可以使用广度优先搜索（BFS）来打印所有节点的值
queue = [inverted_root]
while queue:
    node = queue.pop(0)
    if node:
        print(node.val, end=" ")
        queue.append(node.left)
        queue.append(node.right)


# 输出结果应为：4 7 2 9 6 3 1