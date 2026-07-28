# Methode 1: DFS
# Methode 2: DFS + hash map

#1
# class Solution:
#     def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeeNode:
#         if not preorder or not inorder:
#             return None
#         root = TreeNode()
#         root.val = preorder[0]
#         mid = inorder.index(preorder[0])

#         root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
#         root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

#         return root

#2
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeeNode:
        indices = {val: idx for idx, val in enumerate(inorder)}

        self.pre_idx = 0
        def dfs(l, r):
            if l > r:
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            mid = indices[root_val]
            root.left = dfs(l, mid-1)
            root.right = dfs(mid+1, r)
            return root
        
        return dfs(0, len(inorder)-1)
