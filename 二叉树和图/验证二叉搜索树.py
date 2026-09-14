from typing import Optional
from math import inf
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    pre = -inf
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        # 采用中序遍历
        # 左
        # 在第一次pre = root.val 
        # 因为是递归从小到上，故之后所有值都应该小于pre
        # 此处取 root.val <= pre 返回 False 满足右遍历逻辑
        # 故 右为True 左为False
        if not self.isValidBST(root.left):
            return False
        # 中
        if (root.val <= self.pre):
            return False
        self.pre = root.val
        # 右
        if self.isValidBST(root.right):
            return True
        # return self.isValidBST(root.right)
        return False


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(s.isValidBST(root))  # 输出: True


    s = Solution()
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    print(s.isValidBST(root))  # 输出: False