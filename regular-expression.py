class node(object):
    def __init__(self,attr=None,lchild=None,rchild=None):
        self.lchild = lchild 
        self.rchild = rchild 
        self.attr = attr
    def setlchild(self,lchild):
        self.lchild = lchild
    def setrchild(self,rchild):
        self.rchild = rchild
    def setattr(self,attr):
        self.attr = attr

class bitree(object):
    
    def __init__(self,re):
        self.re = re
        self.relen = len(re)
        self.root = None
        self.createTree()

    def createTree(self):
        if self.relen==0:
            pass
        elif self.relen==1:
            self.root = node(attr=self.re[0]) 
        else: 
            self.root = node(attr=self.re[0])
            prenode = self.root
            for i in range(1,self.relen):
                if self.re[i]=='*':
                    curnode = node(attr=self.re[i-1])
                    prenode.setattr('*')
                    prenode.setrchild(curnode)
                else:
                    curnode = node(attr=self.re[i])
                    prenode.setlchild(curnode)
                    prenode = curnode
                

                    
    def __str__(self):
        treenode = self.root
        orinstr = ''
        while(treenode!=None):
            if treenode.attr=='*':
                orinstr+=(treenode.rchild.attr+treenode.attr)
            else:
                orinstr+=treenode.attr
            treenode = treenode.lchild
        return orinstr

    def ismatch(self,s):
        treenode = self.root
        isInStarState = False
        starNodes = list()
        starIndexes = list()
        i = 0
        while( i!=None and i<len(s) and treenode!=None):
            if isInStarState:
                if treenode.attr!='.' and treenode.attr!=s[i]:
                    treenode = starNodes[len(starNodes)-1].lchild
                    isInStarState = False
                else:
                    i+=1
                    # if i==len(s) and len(starNodes)!=0:
                    #     treenode = starNodes.pop().lchild
                    #     i = starIndexes.pop()
            else:
                if treenode.attr==s[i]:
                    i+=1
                    treenode = treenode.lchild
                elif treenode.attr=='.': 
                    i+=1
                    treenode = treenode.lchild
                elif treenode.attr=='*':
                    isInStarState = True
                    starNodes.append(treenode)
                    starIndexes.append(i)
                    treenode = treenode.rchild
                else:
                    if len(starNodes)==0:
                        break
                    treenode = starNodes.pop().lchild
                    i = starIndexes.pop()
        if i == len(s) and (not isInStarState and treenode==None or isInStarState and starNodes[len(starNodes)-1].lchild==None ):
            return True
        else:
            return False

x = bitree('a*a')
print(x)
y = 'aaaa'
print(x.ismatch(y))
