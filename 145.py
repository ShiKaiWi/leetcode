# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        runtimeStack = list()
        l = []
        r = root
        while r != None :
            if r.left!=None and r.right!=None:
                runtimeStack.append(r)
                runtimeStack.append(r.right)
                r.right = None
                r2 = r.left
                r.left = None
                r = r2
            elif r.left == None and r.right == None:
                l.append(r.val)
                r = runtimeStack.pop() if len(runtimeStack)>0 else None
            elif r.left != None and r.right == None:
                runtimeStack.append(r)
                r2 = r.left
                r.left = None
                r = r2
            else:
                runtimeStack.append(r)
                r2 = r.right
                r.right = None
                r = r2
        return l


root = TreeNode(1)
root.right = TreeNode(2)
print(Solution().postorderTraversal(root))
