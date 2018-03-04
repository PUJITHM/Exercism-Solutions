class BufferFullException(Exception):
    pass

class BufferEmptyException(Exception):
    pass

class CircularBuffer(object):
    def __init__(self, capacity):
        self.buffer = list()
        self.capacity = capacity

    def read(self):
        if self.buffer:
            return self.buffer.pop(0)
        else:
            raise BufferEmptyException('empty..')

    def write(self, data):
        if len(self.buffer) < self.capacity:
            self.buffer.append(data)
        else:
            raise BufferFullException('full..')

    def overwrite(self, data):
        if len(self.buffer) == self.capacity:
            self.buffer.pop(0)
        self.buffer.append(data)

    def clear(self):
        self.buffer = list()