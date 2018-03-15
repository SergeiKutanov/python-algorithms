class MyQueue(object):
    def __init__(self):
        self.inbox = list()
        self.outbox = list()

    def peek(self):
        if len(self.outbox) > 0:
            return self.outbox[-1]
        else:
            if len(self.inbox) > 0:
                return self.inbox[0]
        raise Exception("Queue underflow")

    def pop(self):
        if len(self.outbox) == 0:
            while len(self.inbox) > 0:
                self.outbox.append(self.inbox.pop())
        if len(self.outbox) == 0:
            raise Exception("Queue underflow")
        return self.outbox.pop()

    def put(self, value):
        self.inbox.append(value)