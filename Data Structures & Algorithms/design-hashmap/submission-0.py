class MyHashMap:

    def __init__(self):
        self.lst = [None] * 10

    def put(self, key: int, value: int) -> None:
        index = key%10
        # if new entry in lst
        if self.lst[index] == None:
            node = ListNode(key, value)
            self.lst[index] = node
        # if node exists in array
        else:
            temp = self.lst[index]
            prev = None
            broken = False
            while temp:
                # check if the keys are the same, then replace value
                if temp.key == key:
                    temp.value = value
                    broken = True
                    break
                # continue while keeping track of previous
                else:
                    prev = temp
                    temp = temp.next
            # in case the keys are all different for same index (hash value)
            # set last nodes next to new node
            if not broken:
                prev.next = ListNode(key, value)
                    

    def get(self, key: int) -> int:
        index = key%10
        if self.lst[index] == None:
            return -1
        temp = self.lst[index]
        while temp:
            if temp.key == key:
                return temp.value
            temp = temp.next
        return -1


    def remove(self, key: int) -> None:
        index = key%10
        if self.lst[index] == None:
            return
        temp = self.lst[index]
        # check if the first key is what we are removing
        if temp.key == key:
            self.lst[index] = temp.next
            return
        prev_node = None
        while temp:
            if temp.key == key:
                prev_node.next = temp.next
                return
            prev_node = temp
            temp = temp.next



class ListNode():
    def __init__(self, key, value, node = None):
        self.key = key
        self.value = value
        self.next = node

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)