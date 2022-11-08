class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.front = self.rear = None
        
    def isEmpty(self):
        return self.front == None
    
    def EnQueue(self, item):
        temp = ListNode(item)
        
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

class TreeNode:								
    def __init__ (self, item, left, right):	
        self.data = item				
        self.left = left
        self.right = right
        
    def size(self):
        if self.left:
            left = self.left.size
        else:
            left = 0
            
        if self.right:
            right = self.right.size()
        else:
            right = 0
        return left + right + 1
    
    def depth(self):
        if self.left:
            left_depth = self.left.depth()
        else:
            left_depth = 0
            
        if self.right:
            right_depth = self.right.depth()
        else:
            right_depth = 0
        return max(left_depth, right_depth) + 1
    
    def leaf(self):
        if self.data is None:
            return 0
        elif self.left is None and self.right is None:
            return 1
        else:
            return TreeNode.leaf(self.left) + TreeNode.leaf(self.rignt)
    
    def preorder(self):
        traversal = []
        traversal.append(self.data)
        if self.left:
            traversal += self.left.inorder()
        if self.right:
            traversal += self.right.inorder()
        return traversal

    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self.data)
        if self.right:
            traversal += self.right.inorder()
        return traversal
    
    def postorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        if self.right:
            traversal += self.right.inorder()
        traversal.append(self.data)
        return traversal
    
    def levelorder(self):
        queue = LinkedQueue()
        queue.EnQueue(self.data)
        while not queue.isEmpty():
            n = queue.Dequeue()
            if n is not None:
                print(n.data, end=' ')
                queue.EnQueue(n.left)
                queue.EnQueue(n.right)

class BinaryTree:
    def __init__(self, root):
        self.root = root
    
    def size(self):
        if self.root:
            return self.root.size()
        else:
            return 0
    
    def depth(self):
        if self.root:
            return self.root.depth()
        else:
            return 0
    
    def leaf(self):
        if self.root:
            return self.root.leaf()
        else:
            return 0
    
    def preorder(self):
        if self.root:
            return self.root.prrorder()
        else:
            return []
        
    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []
    
    def postorder(self):
        if self.root:
            return self.root.postorder()
        else:
            return []
    
    def levelorder(self):
        if self.root:
            return self.root.levelorder()
        else:
            return []