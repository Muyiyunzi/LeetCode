# DFS（递归）
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root, now):
            nonlocal ans
            now = (now << 1) + root.val
            if root.left is not None:
                dfs(root.left, now)
            if root.right is not None:
                dfs(root.right, now)
            if root.left is None and root.right is None:
                ans += now
            return
        dfs(root, 0)
        return ans

# 按答案优化了一下DFS
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(root, now):
            if root is None:
                return 0
            now = (now << 1) + root.val
            if root.left is None and root.right is None:
                return now
            return dfs(root.left, now) + dfs(root.right, now)

        return dfs(root, 0)

# 迭代写法（后序遍历）
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = val = 0
        stack = []
        prev = None
        cur = root
        while cur or stack:
            while cur:
                val = (val << 1) + cur.val
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if prev != cur.right and cur.right: # 进入右子树
                stack.append(cur)
                cur = cur.right
            else: # 右子树已访问
                if cur.left is None and cur.right is None:
                    ans += val
                val >>= 1
                prev = cur
                cur = None
        return ans
