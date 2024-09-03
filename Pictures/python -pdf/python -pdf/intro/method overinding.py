class over():
    def method1(self):
        print("hello:")
    def method2(self):
        print("this is a method2:")
class demo(over):
    def method1(self):
        print("hello:1")
        super().method1()
    def method2(self):
        print("this is a method2:")
obj=demo()
obj.method1()
obj.method2()