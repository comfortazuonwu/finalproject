class Queue:
    """ The queue class"""

    def __init__(self):
        """Initialize the queue"""
        self.queue = []

    def enqueue(self,value):
        """Enqueue a value """
        self.queue.append(value)
        


    def dequeue(self,value):
        """Dequeue a value and return it"""
        value = self.queue[0] 
        del self.queue[0]
        return value

    

# Test case
# Scenario: Enqueue three values and then Dequeue it.
# Exepcted Result: It should display 10, 20 , 30 
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

