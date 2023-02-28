# lambda function:
# It is called as anonymous function, when we want to use func concept alone 
# without using func name there we apply concept of lambda func.
# l = [1, 2, 3]
# r = map(lambda x:x+x, l)
# print(list(r))
# res = map(lambda n:pow(n, 2), l)
# print(list(res))
# name = 'manoj'
# (lambda name: print(name)) (name)

# write a program after creating a list with even numbers within the range
# 1 to 15. Now apply lambda function and create a new list which should have 
# square roots of the elements.
# import math
# l1 = []
# for i in range(1, 15):
#     if i % 2 == 0:
#         l1.append(i)
# print(l1)
# # l2 = list(map(lambda n:pow(n, 1/2), l1))
# l2 = list(map(lambda n:math.sqrt(n), l1))
# print(l2)
"""
Four pillars of Oops
1. Abstraction
Hiding the implementation part showing what is required for the users is called as 
abstraction
Eg: exe file
We can make class or method as abstract, opp to abstract is concrete.

2. Encapsulation
Binding data into a single entity
public --- are data that can be accesed by any other class.
private --- can be used where it is declared.
protected --- can be accesed only where it is declared. whichever class inherited
from this class there also we can use.

3. Inheritance
Base class and derived class
Derived class will inherit properties of the base class
base class: parent class
derived class: child class
Types of inheritance:
    1. Single inheritance
    2. Multiple inheritance
    3. Multi level inheritance
    4. Heirarical inheritance
    5. Hybrid inheritance

4. Polymorphism

"""
# ______________Abstraction_______________
# from abc import ABC, abstractmethod
# class abstractDemo(ABC):
#     @abstractmethod
#     def display(self):
#         None
#     @abstractmethod
#     def show(self):
#         None
# class demo(abstractDemo):
#     def display(self):
#         print('Abstraction method')
#     def show(self):
#         print('2nd function')
# obj = demo()
# obj.display()
# obj.show()
# _____________Inheritance________________
# class parent:
#     def display(self):
#         print('Parent class')
# class child(parent):
#     def show(self):
#         print('Child class')
# obj = child()
# obj.display()
# obj.show()
# ____________Single level inheritance_______________
# class A:
#     n = 30
# class B(A):
#     def calc(self):
#         c = self.n + 70
#         print(c)
# obj = B()
# obj.calc()

# ____________Multiple inheritance_______________
# class Mom:
#     def mdisplay(self):
#         print('mom class')
# class Dad:
#     def ddisplay(self):
#         print('dad class')
# class child(Mom, Dad):
#     def cdisplay(self):
#         print('child class')
# obj = child()
# obj.mdisplay()
# obj.ddisplay()
# obj.cdisplay()

# _____________Multi level inheritance_____________
# class grandParent:
#     def display(self):
#         print('Grandparent class')
# class parent(grandParent):
#     def show(self):
#         print('Parent class')
# class child(parent):
#     def printing(self):
#         print('Child class')
# obj = child()
# obj.display()
# obj.show()
# obj.printing()

# ______________Heirarical inheritance_______________
# class parent:
#     def pdisplay(self):
#         print('parent class')
# class child1(parent):
#     def c1show(self):
#         print('child1 class')
# class child2(parent):
#     def c2show(self):
#         print('child2 class')
# c1Obj = child1()
# c2Obj = child2()
# c1Obj.pdisplay()
# c1Obj.c1show()
# c2Obj.pdisplay()
# c2Obj.c2show()

# _______________Hybrid inheritance_________________
# class parent:
#     def pdisplay(self):
#         print('parent class')
# class child1(parent):
#     def c1display(self):
#         print('child1 class')
# class child2(parent):
#     def c2display(self):
#         print('child2 class')
# class kid1(child1):
#     def k1display(self):
#         print('kid1 class')
# class kid2(child1):
#     def k2display(self):
#         print('kid2 class')
# class kid3(child2):
#     def k3display(self):
#         print('kid3 class')
# class kid4(child2):
#     def k4display(self):
#         print('kid4 class')
# k1Obj = kid1()
# k2Obj = kid2()
# k3Obj = kid3()
# k4Obj = kid4()
# print('kid1')
# k1Obj.pdisplay()
# k1Obj.c1display()
# k1Obj.k1display()
# print('kid2')
# k2Obj.pdisplay()
# k2Obj.c1display()
# k2Obj.k2display()
# print('kid3')
# k3Obj.pdisplay()
# k3Obj.c2display()
# k3Obj.k3display()
# print('kid4')
# k4Obj.pdisplay()
# k4Obj.c2display()
# k4Obj.k4display()

# _______________Happy numbers program__________________
# num = input('Enter a number: ')
# print(num)
# l = []
# while num > 3:
#     num = str(num)
#     for digit in num:
#         l.append(digit)
#     for i in range(len(l)):
#         l[i] = int(l[i])
#     sum = 0
#     for j in l:
#         sum += j**2
#     print(sum)  
#     num = sum
# while num > 9:
#     sum = 0
#     for i in range(0, len(str(num)) + 1):
#         r = num % 10
        
        
    




