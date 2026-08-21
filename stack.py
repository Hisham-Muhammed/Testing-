class Stack:

    def __init__(self, size=16):

        self.size = size

        self.data = []

    def push(self, value):

        if len(self.data) >= self.size:

            print("Stack Overflow")

            return False

        self.data.append(value)

        return True

    def pop(self):

        if len(self.data) == 0:

            print("Stack Underflow")

            return None

        return self.data.pop()

    def peek(self):

        if len(self.data) == 0:

            return None

        return self.data[-1]

    def is_empty(self):

        return len(self.data) == 0

    def is_full(self):

        return len(self.data) >= self.size

    def show(self):

        print("Stack:", self.data)
