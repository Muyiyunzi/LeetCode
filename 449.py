# 这题挺好的。没有给明确的构造方法，注意BST的特点，结合后序遍历
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root: return ""
        ans = []
        def postOrder(root):
            if root is None:
                return
            postOrder(root.left)
            postOrder(root.right)
            ans.append(root.val)
            return None
        postOrder(root)
        return " ".join(map(str, ans))      
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data: return None
        nums = list(map(int, data.split(' ')))
        def construct(low, high):
            if nums == [] or nums[-1] < low or nums[-1] > high:
                return None
            val = nums.pop()
            node = TreeNode(val)
            # 先尝试添加至右子树
            node.right = construct(val, high)
            node.left = construct(low, val)
            return node
        return construct(-inf, inf)


        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans