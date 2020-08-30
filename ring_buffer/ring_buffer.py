class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.list = []
        self.counter = 0

    def append(self, item):
        if len(self.list) < self.capacity:
            self.list.append(item)
        else:
            self.list[self.counter] = item
            if self.counter < len(self.list) - 1:
                self.counter += 1
            else:
                self.counter = 0

    def get(self):
        return self.list
