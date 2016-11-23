class test(object):
    y = 3
    def __init__(self):
        self._s = 3


a = test()
a.y = 3
print(a._s)
print(a.y)
