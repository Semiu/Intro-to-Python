# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 21:45:20 2022

@author: Semiu
"""
"""
custom class for a queue that implements the operations enqueue, dequeue, front, rear, and isEmpty with the help of a list
"""
class Queue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self, x):
        return self.queue.insert(0, x)
    
    def dequeue(self):
        return self.queue.pop()
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def front(self):
        return self.queue[-1]
    
    def rear(self):
        return self.queue[0]
    
    
namequeue = Queue()

namequeue.enqueue("Alice")
namequeue.enqueue("Bob")
namequeue.enqueue("Charlie")

print("Info about the queue")
front = namequeue.front()

print(f" -The first priority member is {front}")
rear = namequeue.rear()

print(f" -The last priority member is {rear}")
print("Serving the queue:")
next = namequeue.dequeue()

print(f" -served {next}")
next = namequeue.dequeue()

print(f" -served {next}")
next = namequeue.dequeue()
print(f" -served {next}")