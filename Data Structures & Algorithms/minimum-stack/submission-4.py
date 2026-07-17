class Node:
        def __init__(self,val,m) -> None:
            self.val=val
            self.minimum=m
            self.next:Node
            self.prev:Node

class MinStack:

    def __init__(self):
        self.head=Node(None,None)
        self.st=[]

    def push(self, val: int) -> None:
        m=self.head.minimum
        if m is None:
            n=Node(val,val)
            self.head.next=n
            n.prev=self.head
        elif m<val:
            n=Node(val,m)
            self.head.next=n
            n.prev=self.head
        else:
            n=Node(val,val)
            self.head.next=n
            n.prev=self.head
        
        self.head=self.head.next
        self.st.append(val)



    def pop(self) -> None:
        self.st.pop()
        self.head=self.head.prev

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.head.minimum
