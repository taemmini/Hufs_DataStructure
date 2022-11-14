class ListNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next


MAX_QSIZE = 10


class CircularQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [None] * MAX_QSIZE

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear+1) % MAX_QSIZE

    def EnQueue(self, item):
        if not self.isFull():
            self.rear = (self.rear+1) % MAX_QSIZE
            self.items[self.rear] = item

    def DeQueue(self):
        if not self.isEmpty():
            self.front = (self.front+1) % MAX_QSIZE
            return self.items[self.front]


class TreeNode:
    def __init__(self, item, left, right):
        self.data = item
        self.left = left
        self.right = right

    def size(self):
        if self.left:
            left = self.left.size()
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
            left = self.left.size()
            right = self.right.size()
            return left + right

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
        queue = CircularQueue()
        queue.EnQueue(self.data)
        while not queue.isEmpty():
            n = queue.DeQueue()
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
            return self.root.preorder()
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


# Test
d = TreeNode('D', None, None)
e = TreeNode('E', None, None)
b = TreeNode('B', d, e)
f = TreeNode('F', None, None)
c = TreeNode('C', f, None)
root = TreeNode('A', b, c)
Tree = BinaryTree(root)

print(f' In-Order : {Tree.inorder()}')
print(f'Pre-Order : {Tree.preorder()}')
print(f'Post-Order : {Tree.postorder()}')
print(f'levelorder : {Tree.levelorder()}')

print(f'노드의 개수 = {Tree.size()}개')
print(f'트리의 높이 = {Tree.depth()}')
print(f'단말의 개수 = {Tree.leaf()}개')
