# __________________Stack____________________
# stack = []
# def push_element():
#     el = int(input('Enter a number: '))
#     stack.append(el)
#     print(stack)
# def pop_element():
#     if not stack:
#         print('Stack is already empty')
#     else:
#         e = stack.pop()
#         print('Removed element is: ', e)
#         print(stack)
# while True:
#     choice = int(input('Select an operation: 1. push, 2. pop, 3. exit: '))
#     if choice == 1:
#         push_element()
#     elif choice == 2:
#         pop_element()
#     elif choice == 3:
#         break
#     else:
#         print('Enter a valid input')
        
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# class Stack:
#     def __init__(self):
#         self.head = None
#     def isEmpty(self):
#         if self.head == None:
#             return True
#         else:
#             return False
#     def push(self, data):
#         if self.head == None:
#             self.head = Node(data)
#         else:
#             newNode = Node(data)
#             newNode.next = self.head
#             self.head = newNode
#     def pop(self):
#         if self.isEmpty():
#             return None
#         else:
#             poppedNode = self.head
#             self.head = self.head.next
#             poppedNode.next = None
#             return poppedNode.data
#     def peak(self):
#         if self.isEmpty():
#             return None
#         else:
#             return self.head.data
#     def display(self):
#         t = self.head
#         if self.isEmpty():
#             print('Stack underflow')
#         else:
#             while t != None:
#                 print(t.data, end = ' ')
#                 t = t.next
#                 if(t != None):
#                     print(' -> ', end = ' ')
#             return
# if __name__ == '__main__':
#     s = Stack()
#     s.push(1)
#     s.push(2)
#     s.push(3)
#     s.push(4)
#     s.display()
#     print(s.peak())
#     s.pop()
#     s.pop()
#     s.display()

# str = input('')
# res = True
# for i in str:
#     if i == '[' and str.__contains__(']'):
#         if (str.index(']') - i.index())%2 != 0:
#             continue
#         else:
#             res = False
#             break
# print(res)

# _________________Checking balanced parameters in a stack__________________
# s = input()
# st = []
# balanced = True
# for i in s:
#     if (i == '[' or i == '{' or i == '('):
#         st.append(i)
#     elif(i == ']'):
#         if(len(st) and st.pop() != '['):
#             balanced = False
#             break
#     elif(i == '}'):
#         if(len(st) and st.pop() != '{'):
#             balanced = False
#             break
#     elif(i == ')'):
#         if(len(st) and st.pop() != '('):
#             balanced = False
#             break
#     else:
#         balanced = False
#         break
# if (len(st) or balanced == False):
#     print(balanced)
# else:
#     print(balanced)

# ____________Queue using array or list_____________
# queue = []
# def enqueue():
#     el = input('Enter element: ')
#     queue.append(el)
#     print(el, 'is added in q')
# def dequeue():
#     if not queue:
#         print('Q is emply')
#     else:
#         e = queue.pop(0)
#         print('removed element: ', e)
# def display():
#     print(queue)
# while True:
#     print('Select operation 1. add, 2. remove, 3. show, 4. exit: ')
#     choice = int(input())
#     if choice == 1:
#         enqueue()
#     elif choice == 2:
#         dequeue()
#     elif choice == 3:
#         display()
#     elif choice == 4:
#         break
#     else:
#         print('Enter a valid input: ')

# ____________________________________________________  
# from queue import LifoQueue
# l = LifoQueue(maxsize=5)
# print(l.qsize())
# l.put('a')
# l.put('b')
# l.put('c')
# print(l.full())
# print(l.qsize())
# print(l.get())
# print(l.get())
# print(l.get())
# print(l.empty())

# ____________________________________________________
# import queue
# print(queue)
# l = queue.Queue(maxsize=5)
# l.put(10)  
# l.put(20)
# print(l.get())
# print(l.get())

# ____________________________________________________
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.head = None
        self.last = None
    def enqueue(self, data):
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last = self.last.next
    def dequeue(self, data):
        if self.head is None:
            return None
        else:
            to_return = self.head.data
            self.head = self.head.next
            return to_return
aQueue = Queue()
while True:
    print('enqueue <value>')
    print('dequeue')
    print('quit')
    do = input('What would you like to do? ').split()
    operation = do[0].strip().lower()
    if operation == 'enqueue':
        aQueue.enqueue(int(do[1]))
    elif operation == 'dequeue':
        dequeued = aQueue.dequeue()
        if dequeued == None:
            print('Queue is empty')
        else:
            print('Dequeued element: ', int(dequeued))
    elif operation == 'quit':
        break
    else:
        print('Invalid Input')
            
        



  

        

        
        
    
        
        
        