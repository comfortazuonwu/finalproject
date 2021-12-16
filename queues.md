**Queues**

**Introduction**

A Queue is a linear structure which follows the order in which the operations are performed. The order is First In First Out (FIFO). In a queue, we remove the item the least recently added. A real world example of a queue is any queue of consumers for a resource where the consumer that came first is served first. 

**Types of Queues**

- Simple Queue
- Circular Queue
- Priority Queue
- Double Ended Queue


**Simple Queue**

A simple queue strictly follows the FIFO rule (removal at the front, insertion at the rear)

![simple queue](simple-queue.jpg)



**Circular Queue**

In a circular queue, the last element points to the first element making a circular link.

![circular queue](circular-queue.jpg)

**Priority Queue**

In a priority queue, insertion occurs based on the arrival of the values and removal occurs based on priority.

![priority queue](priority-queue.jpg)


**Double Ended Queue**

In a double ended queue, insertion and removal of elements can be performed from either from the front or rear. Thus, it does not follow the FIFO (First In First Out) rule.

![double ended queue](dequeue.jpg)





**Queue Operations in Python**

| Queue Operations| Explanation                           | Example                       | Performance           |
| ----------------| ------------------------------------- | ----------------------------- |---------------------- |
| enqueue         | It adds value to the back of the queue. Uses the append() method| queue.append(x) |  O(1)     |
| dequeue         | Remove and return the item from the front of the queue or pop off index 0. Uses the pop() method|queue.pop(0)| O(n) ||                                 
|   size          |Returns the size of a queue. Uses the len() method|size = len(queue)|   O(1)                       |                       

 Below is an example of how queue works in python. This gives a good explanation of the First In, First Out rule.

```python

"""Initialize the queue"""
queue = []

""" Add values to the queue"""
queue.append('first')
queue.append('second')
queue.append('third')
queue.append('fourth')

print('First queue')
print(queue)

"""Remove values from the queue"""
print('\nValues removed from the queue')
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

"""Display the new queue"""
print('\nNew Queue')
print(queue)

"""code output"""

First queue
['first', 'second', 'third', 'fourth']

Values removed from the queue
first
second
third

New Queue
['fourth']

```

We can see that the value 'first' was dequeued first because it was enqueued first.

**Problem to solve**

Input the code needed to enqueue and dequeue the values

```python
class Queue:
    """ The queue class"""

    def __init__(self):
        """Initialize the queue"""
        self.queue = []

    def enqueue(self,value):
        """Enqueue a value """
        pass
        


    def dequeue(self,value):
        """Dequeue a value and return it"""
        pass

    

# Test case
# Scenario: Enqueue three values and then Dequeue it.
# Expected Result: It should display 10,20,30 
print("Test 1")
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

value = queue.dequeue(0)
print(value)
value = queue.dequeue(0)
print(value)
value = queue.dequeue(0)
print(value)

```
Take a look at the [solution](queuessolution.py) when you are done.