import copy
class qsort(object):
    def __init__(self,A=None,order=True):
        """
        order=true means from small to big
        """

        self.A = copy.copy(A)
        self.order = order

    def setOrder(self,neworder):
        self.order = neworder

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
        
    def sub_qsort(self,p,q):
        if p<q:
            r = self.partition(p,q)
            self.sub_qsort(p,r-1)
            self.sub_qsort(r+1,q)
    def sort(self):
        self.sub_qsort(0,len(self.A)-1)
        if self.order:
            return self.A
        else:
            return [self.A[i] for i in range(len(self.A)-1,-1,-1)]


if __name__ == "__main__":
    A = list((3,8,2,4,9,10))
    Aqsort = qsort(A,True)
    A_order = Aqsort.sort()
    print(A)
    print(A_order)
    Aqsort.setOrder(False)
    print(Aqsort.sort())



