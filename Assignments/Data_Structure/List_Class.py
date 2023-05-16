class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node=SLNode(val)
        new_node.next = self.head
        self.head = new_node


class SLNode:
    def __init__(self,val):
        self.value = val
        self.next = None