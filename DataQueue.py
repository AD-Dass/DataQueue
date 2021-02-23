
class Queue(): #First in - First out
    def __init__(self,queue_size): #initialise the queue
        self.queue = []
        self.cap = queue_size

    def push(self,data_input): #add stuff to the queue
        if len(self.queue) < self.cap: #conditional statement to see if the queue is full
            self.queue.append(data_input)
            print('New item added to the queue')
        else: 
            print('Queue is full')

    def pull(self): #Pull from the queue
        data_output = self.queue.pop(0)
        return data_output

    def empty(self): #Empty the queue for whatever reason you may need
        for i in range(len(self.queue)):
            self.queue.pop(-1)
        print('Queue has been emptied')

    def show(self): #print the queued list.
        print(self.queue)


        
