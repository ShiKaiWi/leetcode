class stack(object):
    def __init__(self,capacity=100):
        self.capacity = capacity
        self.stack = list()
        self.size = 0
        self.top = 0

    def push(self,element=None):
        if element!=None:

