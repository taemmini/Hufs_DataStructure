class Node:
     
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedQueue:
 
    def __init__(self):
        self.front = self.rear = None
 
    def isEmpty(self):
        return self.front == None
 
    def EnQueue(self, item):
        temp = Node(item)
 
        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp
 
    def DeQueue(self):
        if not self.isEmpty():
            temp = self.front
            self.front = temp.next
            return temp.data
    
    def Peek(self):
        if self.isEmpty():
            return 'Stack is empty.'
        return self.front.data
    
    def Display(self, string):
        print(string, end='')
        node = self.front
        while node:
            print(node.data, end=' ')
            node = node.next
        print()

# Test Dirve by professor
def testLinkedQueue():
    print('연결된 구조의 큐 구현\n')
    Queue = LinkedQueue()
    for i in range(10):
        Queue.EnQueue(i)
    Queue.Display('큐 EnQueue 9회: ')
    print(f'\tDeQueue() → {Queue.DeQueue()}')
    print(f'\tDeQueue() → {Queue.DeQueue()}')
    print(f'\tDeQueue() → {Queue.DeQueue()}')
    Queue.Display('큐 DeQueue 3회: ')
    
    Queue.EnQueue('수퍼맨')
    Queue.EnQueue('배트맨')
    Queue.EnQueue('원더우먼')
    Queue.EnQueue('아쿠아맨')
    Queue.Display('큐 EnQueue 4회: ')
    print(f'\tDeQueue() → {Queue.DeQueue()}')
    Queue.Display('큐 DeQueue 1회: ')
    print(f'\tpeek() → {Queue.Peek()}')
    
testLinkedQueue()