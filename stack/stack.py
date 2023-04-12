class Stack:
    
    def __init__(self, cap):
        self.top = 0
        self.capacity = cap
        self.items = []

    def is_empty(self):
        if (self.top == 0):
            return True
        return False

    def push(self, item):
        try:
            if (self.top == self.capacity):
                raise IndexError
            else:
                self.top += 1
                self.items.append(item)
        except IndexError:
            print("[Error]: Overflow detected.")

    def pop(self):
        try:
            if (self.is_empty()):
                raise IndexError
            else:
                self.top -= 1
                return self.items.pop()
        except IndexError:
            print("[Error]: Underflow detected.")

    def peek(self):
        return self.items[self.top - 1]

    def showAll(self):
        return(self.items)