class a():
    count = 0
    def __init__(self):
        self.x = a.count
        a.count = a.count+5
    def aksh(self):
        print(a.count,self.x)
    

print(a.count)
x = a()
x.aksh()
y = a()
y.aksh()

