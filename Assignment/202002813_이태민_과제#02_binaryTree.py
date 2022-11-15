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


# Test
d = TreeNode('D', None, None)
e = TreeNode('E', None, None)
b = TreeNode('B', d, e)
f = TreeNode('F', None, None)
c = TreeNode('C', f, None)
root = TreeNode('A', b, c)
Tree = BinaryTree(root)


print("트리의 순회 4가지")
print(f'In-Order : {Tree.in_order()}')
print(f'Pre-Order : {Tree.pre_order()}')
print(f'Post-Order : {Tree.post_order()}')
print(f'Level-order : {Tree.level_order()}')

print("\n트리의 구성요소 판단")
print(f'노드의 개수 = {Tree.size()}개')
print(f'트리의 높이 = {Tree.depth()}')
print(f'단말의 개수 = {Tree.leaf()}개')
