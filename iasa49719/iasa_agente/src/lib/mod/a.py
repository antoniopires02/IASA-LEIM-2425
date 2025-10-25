class A:
    def __init__(self):
        self.a1 = 0
        
    def __hash__(self):
        h = super().__hash__()
        print("__hash__: ", h)
        return h
    
d = {}
a1 = A()
d[a1] = 10
    
print(">", d[a1])
    