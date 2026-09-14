from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 中左右 左中右
        def recur(root,left,right):
            if left > right:return 
            #根节点
            node = TreeNode(preorder[root])
            # 划分根节点，左子树
            # inorder的preorder[root] 左侧为左子树
            m = dic[preorder[root]]
            # 左子树 root+1 在preorde中是 左子树的root
            node.left = recur(root+1,left,m-1)
            # 右子树 m-left当前左子树的长度
            # root + (m-left) + 1 = 右子树root
            node.right = recur(root + (m-left) + 1,m+1,right)
            return node
        dic,preorder = {},preorder
        #记录中序遍历 对应的位置
        for i in range(len(inorder)):
            dic[inorder[i]] = i
        return recur(0,0,len(inorder)-1)


if __name__ == "__main__":
    s = Solution()
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    root = s.buildTree(preorder, inorder)
    # 输出: [3,9,20,null,null,15,7]
    print(root.val)  # 输出: 3
    print(root.left.val)  # 输出: 9
    print(root.right.val)  # 输出: 20
    print(root.right.left.val)  # 输出: 15
    print(root.right.right.val)  # 输出: 7