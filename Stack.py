class Stack:
    def _init_(self):
        self.items = []
    def push (self, item):
        self.items.append(item)
    def pop (self):
        return self.items.pop()
    def isEmpty(self):
        return self.items == []
    def get_stack(self):
        return self.items
s = Stack()
s.push("A")
s.push("B")
s.push("C")
s.pop("D")
print(s.get_Stack())