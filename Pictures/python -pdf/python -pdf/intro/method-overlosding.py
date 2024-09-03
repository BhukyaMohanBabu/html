class A():
    def method(self,a,b,c):
        return a+b+c
    def method(self,a,b,c,d=20):
        return a+b+c+d
obj=A()
print(obj.method(10,10,10))
