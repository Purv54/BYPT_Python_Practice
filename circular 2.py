class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.items = [None] * size
        self.front = self.rear = -1
    
    def insert(self, value):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")
            return
        elif self.front == -1:
            self.front = self.rear = 0
            self.items[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.size
            self.items[self.rear] = value
        

    def delete(self):
        if self.front == -1:
            print("Queue is empty")
            return
        elif self.front == self.rear:
            print(self.items[self.front])
            self.front = self.rear = -1
        else:
            print(self.items[self.front])
            self.front = (self.front + 1) % self.size

q = CircularQueue(6)

q.insert(1)
q.insert(2)
q.insert(3)
q.insert(4)
q.insert(5)

q.delete()
q.delete()
q.delete()
q.delete()
q.delete()
q.insert(6)
q.insert(1)
print(q.items)
        

    

  