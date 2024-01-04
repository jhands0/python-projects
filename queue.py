class Queue():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0,item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


q = Queue()
q.push(2)
q.push(5)
q.pop()
print(q.peek())