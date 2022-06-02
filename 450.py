# 按答案分类讨论
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif root.left is None or root.right is None:
            root = root.left if root.left else root.right
        else:
            successor = root.right
            while successor.left:
                successor = successor.left

            # 注意，这句话right必须在left前边，因为此时successor左子树为空，不能先接一个左子树上去再向右递归删，否则会出错
            successor.right = self.deleteNode(root.right, successor.val)
            successor.left = root.left
            return successor
        return root



# 答案改进版，左右子树都有的时候不用再递归了
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif root.left is None or root.right is None:
            root = root.left if root.left else root.right
        else:
            successor = root.right
            prev = root
            while successor.left:
                prev = successor
                successor = successor.left
            root.val = successor.val
            if prev != root:
                prev.left = successor.right
            else:
                prev.right = successor.right
        return root
