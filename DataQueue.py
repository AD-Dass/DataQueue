
class Queue():
    def __init__(self,queue_size):
        self.queue = []
        self.cap = queue_size

    def push(self,data_input):
        if len(self.queue) < self.cap:
            self.queue.append(data_input)
            print('New item added to the queue')
        else:
            print('Queue is full')

    def pull(self):
        data_output = self.queue.pop(0)
        return data_output

    def empty(self):
        for i in range(len(self.queue)):
            self.queue.pop(-1)
        print('Queue has been emptied')

    def show(self):
        print(self.queue)

if __name__=='__main__':
    MyQueue = Queue(3)
    MyQueue.push(1)
    MyQueue.push(2)
    MyQueue.push(3)
    MyQueue.push(4)
    MyQueue.show()
    iasked=MyQueue.pull()
    print(iasked)
    iasked=MyQueue.pull()
    print(iasked)
    iasked=MyQueue.pull()
    print(iasked)
    MyQueue.push(4)
    MyQueue.show()
    MyQueue.empty()
    MyQueue.show()
        
