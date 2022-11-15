class ArrayQueue:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)


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

# 전위 순회
    def pre_order(self):
        traversal = []
        traversal.append(self.data)
        if self.left:
            traversal += self.left.pre_order()
        if self.right:
            traversal += self.right.pre_order()
        return traversal

# 중위 순회
    def in_order(self):
        traversal = []
        if self.left:
            traversal += self.left.in_order()
        traversal.append(self.data)
        if self.right:
            traversal += self.right.in_order()
        return traversal

# 후위 순회
    def post_order(self):
        traversal = []
        if self.left:
            traversal += self.left.post_order()
        if self.right:
            traversal += self.right.post_order()
        traversal.append(self.data)
        return traversal

# 레벨 순회
    def level_order(self):
        traversal = []
        queue = ArrayQueue()

        if self.data:
            queue.enqueue(self)

        while not queue.isEmpty():
            node = queue.dequeue()
            traversal.append(node.data)

            if node.left:
                queue.enqueue(node.left)

            if node.right:
                queue.enqueue(node.right)

        return traversal


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

    def pre_order(self):
        if self.root:
            return self.root.pre_order()
        else:
            return []

    def in_order(self):
        if self.root:
            return self.root.in_order()
        else:
            return []

    def post_order(self):
        if self.root:
            return self.root.post_order()
        else:
            return []

    def level_order(self):
        if self.root:
            return self.root.level_order()
        else:
            return []


# Test1
d = TreeNode("D", None, None)
b = TreeNode("B", d, None)
g = TreeNode("G", None, None)
h = TreeNode("H", None, None)
e = TreeNode("E", g, h)
f = TreeNode("F", None, None)
c = TreeNode("C", e, f)
root1 = TreeNode("A", b, c)

Tree1 = BinaryTree(root1)

print("첫번째 트리의 순회 4가지")
print(f'In-Order : {Tree1.in_order()}')
print(f'Pre-Order : {Tree1.pre_order()}')
print(f'Post-Order : {Tree1.post_order()}')
print(f'Level-order : {Tree1.level_order()}')

print("\n첫번째 트리의 구성요소 판단")
print(f'노드의 개수 = {Tree1.size()}개')
print(f'트리의 높이 = {Tree1.depth()}')
print(f'단말의 개수 = {Tree1.leaf()}개')

# Test2
a = TreeNode("A", None, None)
b = TreeNode("B", None, None)
divide1 = TreeNode("/", a, b)
c = TreeNode("C", None, None)
multi1 = TreeNode("*", divide1, c)
d = TreeNode("D", None, None)
multi2 = TreeNode("*", multi1, d)
e = TreeNode("E", None, None)
root2 = TreeNode("+", multi2, e)

Tree2 = BinaryTree(root2)

print("\n두번째 트리의 순회 4가지")
print(f'In-Order : {Tree2.in_order()}')
print(f'Pre-Order : {Tree2.pre_order()}')
print(f'Post-Order : {Tree2.post_order()}')
print(f'Level-order : {Tree2.level_order()}')

print("\n두번째 트리의 구성요소 판단")
print(f'노드의 개수 = {Tree2.size()}개')
print(f'트리의 높이 = {Tree2.depth()}')
print(f'단말의 개수 = {Tree2.leaf()}개')
