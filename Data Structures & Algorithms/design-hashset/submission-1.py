class MyHashSet:

    def __init__(self):
        self.h=[[] for _ in range(32)]
        self.size=32

    def add(self, key: int) -> None:
        for i in self.h[key%self.size]:
            if i==key:
                return
        self.h[key%self.size].append(key)        

    def remove(self, key: int) -> None:
        for i in range(len(self.h[key%self.size])):
            if self.h[key%self.size][i]==key:
                self.h[key%self.size].pop(i)
                return

    def contains(self, key: int) -> bool:
        for i in range(len(self.h[key%self.size])):
            if self.h[key%self.size][i]==key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)