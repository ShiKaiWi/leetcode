# Definition for a binary tree node.
"""
leetcode will set the recursion limit automatically
"""
# import sys
# sys.setrecursionlimit(10000)

"""
leetcode will include the definition of TreeNode
so your definition shouldnot be given otherwise a runtime error will be raised
"""
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    """
    leetcode will build the level travel tree automatically
    so you needn't do this
    """

    # def height(self,root):
    #     if root==None:
    #         return 0
    #     hl = self.height(root.left)
    #     hr = self.height(root.right)
    #     h = hl if hl>hr else hr
    #     return h+1 

    # def buildLevelOrderTree(self,tree,level):
    #     if level==0:
    #         self.l.append(tree.val if tree!=None else None)
    #         return
    #     if tree==None:
    #         return
    #     self.buildLevelOrderTree(tree.left,level-1)
    #     self.buildLevelOrderTree(tree.right,level-1)

    def buildTree(self,preorder,inorder):
        self.preorder = preorder
        self.inorder = inorder
        self.indexes = dict((inorder[i],i) for i in range(0,len(inorder)))
        root = self.buildTreeSub(0,0,len(preorder)-1)
        # h = self.height(root)
        # self.l = []
        # for i in range(0,h):
        #     self.buildLevelOrderTree(root,i)
        # i = len(self.l) - 1
        # while i>=0 and self.l[i]==None :
        #     self.l.pop()
        #     i-=1
        return root  


    # def buildArrayTree(self,l,root):
    #     l.append(root.left.val if root.left != None else None)
    #     l.append(root.right.val if root.right!= None else None)
    #     if root.left!=None:
    #         self.buildArrayTree(l,root.left)
    #     if root.right!=None:
    #         self.buildArrayTree(l,root.right)

    def buildTreeSub(self,prestart,instart,inend):
        if prestart>len(self.preorder)-1 or inend<instart:
            return
        root = TreeNode(self.preorder[prestart])
        
        index = self.indexes[root.val]
        root.left = self.buildTreeSub(prestart+1,instart,index-1)
        root.right = self.buildTreeSub(prestart+index-instart+1,index+1,inend)
        return root

