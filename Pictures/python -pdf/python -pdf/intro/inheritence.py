'''inheritance is the process of inheriting properties from a parent class into a child class
there are four types of inheritance 
1.single inheritance: in single inheritance ,a child class inherits from the parent class ,here
 only one child and one parent calss'''
 
class parent:
    def method1(self):
        print("This is a parent class...!!!")
class child(parent) :
    def method2(self):
        print("this is a child class")
#calling
calling=child()
calling.method1()
calling.method2() 
'''
2.multiple inheritance: in multiple inheritance ,a child class inherits from multiple parent classess ,here 
one child class and multiple parents class'''


class mother:
    def __init__(self):
        print("this is a mother class:")
class father:
    def method2 (self):
        print("this is a father class")
class child(mother,father):
    def method3(self):
        print("this is a child class")
calling=child()
calling.method2()
calling.method3() 

'''

3.multilevel inheritance: in multilevel inheritance ,suppose A ,B, and c ,  A is the super class b is the 
child of class A and c is the child of class B '''
class Parent:
    def method2(self):
        print("this is a parent1 class :")
    def __init__(self):
        print("this is also a parent one class:")
        super()
class parent2(Parent):
    def method1(self):
        print("this is a parent2 class")
class child1(parent2):
    def method3(self):
        print("this is a child class:")
calling=child1()
calling.method2()
calling.method1()
calling.method3()
'''
4.hieranchical inheritance: in hierarchiacal inheritance ,a multiple child class inheriting 
from the single parent class..here multiple child class and single parent class
'''
class parent:
    def method1(self):
        print("this is a parent class:")
class child1(parent):
    def method2(self):
        print("this is a child one class:")
class child2(parent):
    def method3(self):
        print("this is a child2 class")
call=child1()
call.method1()
call.method2()
calling=child2()
calling.method3()

