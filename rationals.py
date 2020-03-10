def all_rationals(n):
    class Queue:
        def __init__(self):
            self.items = []

        def enqueue(self, item):
            self.items.insert(0, item)

        def dequeue(self):
            if not self.isEmpty():
                return self.items.pop(-1)

        def isEmpty(self):
            return len(self.items)==0

        def __len__(self):
            return self.size()

        def peek(self):
            if not self.isEmpty():
                return self.items[-1].data

        def size(self):
            return len(self.items)

    class node:
        def __init__(self,data):
            self.data = data
            self.left = None
            self.right = None

    def insertNodes(root,i,n):
            tup = root.data
            left_node =node((tup[0], tup[0]+tup[1]))
            right_node=node((tup[0]+tup[1], tup[1]))

            if i<n:
                root.left = insertNodes(left_node,i+1,n)
                root.right = insertNodes(right_node,i+1,n)
            return root




    def levelOrder(start):
        if start== None:
            return "error"

        queue = Queue()
        queue.enqueue(start)

        traversal = []
        while len(queue) > 0:
            traversal.append(queue.peek())
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal
    

    data = (1, 1)
    i = 1

    root = node(data)

    tree = insertNodes(root,i,n)
    
    arr = levelOrder(tree)
    
    return arr
