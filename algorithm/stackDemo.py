class Stack:
    """a simple implementation of the stack data structure"""
    def __init__(self, e):
        print("Initialized Stack")
        self.elements = []
        self.elements = e

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        return self.elements.pop(-1)