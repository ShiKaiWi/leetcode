from qsort import qsort
import copy
class findithminmal(object):
    def __init__(self,A=None):
        self.A = copy.copy(A)

    def partition(self,p,q):
        x = self.A[q]
        r = p-1
        for i in range(p,q):
            if self.A[i]<x:
                r += 1
                temp = self.A[r]
                self.A[r] = self.A[i]
                self.A[i] = temp
        
        temp = self.A[r+1]
        self.A[r+1] = x
        self.A[q] = temp
        return r+1
 
    def subFind(self,i,p,q):
        if p<q:
            r = self.partition(p,q)
            if i+p==r+1:
                return self.A[r]
            elif i+p<r+1:
                return self.subFind(i,p,r-1)
            else:
                return self.subFind(i-(r-p)-1,r+1,q)
        if p==q:
            return self.A[p]

    def find(self,i):
        if i<1 or i>len(A):
            return "invalid parameter"
        return self.subFind(i,0,len(self.A)-1)


if __name__=="__main__":
    A = list((2,3,9,4,10,4))
    fd = findithminmal(A)
    qa = qsort(A)
    print(fd.find(7))
    print(qa.sort())

