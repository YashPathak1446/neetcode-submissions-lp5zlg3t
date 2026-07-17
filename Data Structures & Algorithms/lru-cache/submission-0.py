class ListNode():
    def __init__(self, key = None, val = None):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = dict()

        self.head = ListNode()
        self.tail = ListNode()
        self.head.right = self.tail
        self.tail.left = self.head
    
    
    def insert(self, leftNode, node, rightNode):
        self.map[node.key] = node
        leftNode.right = node
        node.left = leftNode
        node.right = rightNode
        rightNode.left = node

    
    def remove(self, leftNode, node, rightNode):
        del self.map[node.key]
        leftNode.right = rightNode
        rightNode.left = leftNode
        node.right = None
        node.left = None
        return node


    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        rightNode = node.right
        leftNode = node.left
        node = self.remove(leftNode, node, rightNode)
        self.insert(self.head, node, self.head.right)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if self.head.right is self.tail:
            temp = ListNode(key, value)
            self.insert(self.head, temp, self.tail)
        
        elif key not in self.map: 
            if len(self.map) < self.capacity:
                temp = ListNode(key, value)
                self.insert(self.head, temp, self.head.right)
            
            else:
                removed = self.remove(self.tail.left.left, self.tail.left, self.tail)
                node = ListNode(key, value)
                self.insert(self.head, node, self.head.right)
        
        else:
            node = self.map[key]
            removed = self.remove(node.left, node, node.right)
            self.insert(self.head, node, self.head.right)
            node.val = value
            self.map[key] = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)