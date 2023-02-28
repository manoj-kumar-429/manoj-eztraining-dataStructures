# # ______________Happy numbers_________________
# def happy(n):
#     s = r = 0
#     while(n >= 0):
#         for i in range(0, len(str(n))):
#             r = n % 10
#             s = s + r**2
#             n = n // 10
#         return s
# num = int(input('Enter a number: '))
# res = num
# while(res != 1 and res != 4):
#     res = happy(res)
# if res == 1:
#     print('Happy number')
# else: 
#     print('Not a happy number')
# _______________Protected_________________
# class encap:
#     _a = 10
#     c = 20
#     def encapFunction(self):
#         _b = 200
#         print('Encap function accessing protected')
#         print(self._a+10)
# obj = encap()
# print(obj._a)
# obj.encapFunction()
# print(obj.c)

# ________________Private___________________
# class encap:
#     __a = 10
#     print(__a)
#     def encapFunc(self):
#         print(self.__a + 12)
# obj = encap()
# obj.encapFunc()
# print(obj.__a)

"""
Polymorphism:
One item or same item used for different purposes.
Types:
1. Overloading
    i. Operator overloading
    Eg: The + operator is used for both addition and for the string concatenation.
    ii. Method overloading
    Eg: Using the same function for multiple cases like one with no arguments, another
    with few arguments and one with all the arguments.
2. Overriding
If a method is defective or cant be used inside derived class it will take it from 
its base class or parent class.
"""

# _______________Method overloading________________
# class moverload:
#     def display(self, a = None, b = None):
#         print(a, b)
# obj = moverload()
# print('Without Arguments')
# obj.display()
# print('With Arguments')
# obj.display(10, 20)
# print('With One Argument')
# obj.display(30)

# class vjw:
#     def placename(self):
#         print('Vjw placename is KLU')
#     def student(self):
#         print('Yes - vjw')
#     def which_year(self):
#         print('3rd year')
# class hyd:
#     def placename(self):
#         print('Hyd placename is HYD - KLU')
#     def student(self):
#         print('Yes - hyd')
#     def which_year(self):
#         print('3rd year - hyd')
# obj_vjw = vjw()
# obj_hyd = hyd()
# for details in (obj_vjw, obj_hyd):
#     details.placename()
#     details.student()
#     details.which_year()

# ________________________________________________________
# ________________________________________________________
# ____________________Data Structures_____________________
# ________________________________________________________
# ________________________________________________________
"""
Helps to write efficient programs
Linear - Storing data sequentially
(Array, Linked List, Stack, Queue & Matrix)
linear - Static (Array), Dynamic (List, Queue, Stack)
Non Linear - No sequential style required
(Binary Tree, Heap, Hash Table & Graph)

Linked list:
Eg: Train
As the name says list of items which are linked with one another is called
as linked list.
Types: 
    Single / singly linked list
    Double / doubly linked list
    Circular

Creating linked list:
step - 1: Create the node
step - 2: Partition the node with 2 segments data & None
step - 3: Add value into the blank node
step - 4: Mark the node as head
step - 5: Create the next node by following the above steps
step - 6: Establish link btw the 1st node and the 2nd node

Display linked list:
Traversal is required from first node till tail node in order to display
existing linked list.
"""




