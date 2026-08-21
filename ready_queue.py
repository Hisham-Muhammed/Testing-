class ReadyQueue:

    def __init__(self):

        self.queue = []


    def enqueue(self, process):

        self.queue.append(process)


    def dequeue(self):

        if self.is_empty():

            return None

        return self.queue.pop(0)


    def peek(self):

        if self.is_empty():

            return None

        return self.queue[0]


    def is_empty(self):

        return len(self.queue) == 0


    def size(self):

        return len(self.queue)


    def remove(self, process):

        if process in self.queue:

            self.queue.remove(process)


    def show(self):

        print(
            "Ready Queue:",
            [process.pid for process in self.queue]
        )
