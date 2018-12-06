class Queue(object):
    '''队列'''
    def __init__(self):
        self.items = []
    def is_pmpty(self):
        return self.items == []

    def enqueue(self,item):
        '''建造队列'''
        self.items.insert(1,item)

    def dequeue(self):
        '''出队列'''
        return self.items.pop()
    def size(self):
        '''返回大小'''
        return len(self.items)
if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(3)
    q.enqueue(5)
    print(q.dequeue())
    print(q.size())