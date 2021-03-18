
def validBracketSequence(sequence):
    
    # define opening and closing chars
    open_char = ("(", "[", "{")
    close_char = (")", "]", "}")
    
    stack = []
    
    # iterate over chars in sequence
    for char in sequence:
        
        if char in open_char:
            stack.append(char)
        elif char in close_char:
            pos = close_char.index(char)
            if len(stack) > 0 and open_char[pos] == stack[len(stack) - 1]:
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def queueOnStacks(requests):
    left = Stack()
    right = Stack()

    def insert(x):
        left.push(x)

    def remove():
        # check if right stack is empty
        if len(right.items) == 0:
            while len(left.items) > 0:
                right.push(left.pop())
            if len(right.items) == 0:
                return None 
        # then return right stack item
        return right.pop()

    ans = []
    for request in requests:
        req = request.split(" ")
        if req[0] == 'push':
            insert(int(req[1]))
        else:
            ans.append(remove())
    return ans
