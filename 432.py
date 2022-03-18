# 回来补课！不就是双向链表+哈希吗，我这里是一个个node，node里不带词典，反而更快些
class Node:
    def __init__(self, key: str):
        self.next = None
        self.prev = None
        self.key = key
        self.value = 1

class AllOne:

    def __init__(self):
        self.keys = {}
        self.root = Node("")
        self.root.next = self.root
        self.root.prev = self.root
        self.root.key = ""

    def inc(self, key: str) -> None:
        if key not in self.keys:
            tmp = Node(key)
            tmp.prev = self.root
            tmp.next = self.root.next
            tmp.next.prev = tmp
            tmp.prev.next = tmp
            self.keys[key] = tmp
        else:
            tmp = self.keys[key]
            tmp.value += 1
            # value+1, swap with next
            while(tmp.next is not self.root and tmp.next.value < tmp.value):
                nxt = tmp.next
                nxt.prev = tmp.prev
                tmp.next = nxt.next

                tmp.prev.next = nxt
                nxt.next.prev = tmp

                tmp.prev = nxt
                nxt.next = tmp

    def dec(self, key: str) -> None:
        tmp = self.keys[key]
        tmp.value -= 1
        # value-1, swap with last
        if not tmp.value:
            tmp.prev.next = tmp.next
            tmp.next.prev = tmp.prev
            del self.keys[key]
        else:
            while(tmp.prev is not self.root and tmp.prev.value > tmp.value):
                prv = tmp.prev
                prv.next = tmp.next
                tmp.prev = prv.prev

                tmp.next.prev = prv
                prv.prev.next = tmp

                tmp.next = prv
                prv.prev = tmp

    def getMaxKey(self) -> str:
        return self.root.prev.key

    def getMinKey(self) -> str:
        return self.root.next.key

# 最开始CV大法的标准答案
class Node:
    def __init__(self, key="", count=0):
        self.prev = None
        self.next = None
        self.keys = {key}
        self.count = count

    def insert(self, node: 'Node') -> 'Node':  # 在 self 后插入 node
        node.prev = self
        node.next = self.next
        node.prev.next = node
        node.next.prev = node
        return node

    def remove(self):  # 从链表中移除 self
        self.prev.next = self.next
        self.next.prev = self.prev

class AllOne:
    def __init__(self):
        self.root = Node()
        self.root.prev = self.root
        self.root.next = self.root  # 初始化链表哨兵，下面判断节点的 next 若为 self.root，则表示 next 为空（prev 同理）
        self.nodes = {}

    def inc(self, key: str) -> None:
        if key not in self.nodes:  # key 不在链表中
            if self.root.next is self.root or self.root.next.count > 1:
                self.nodes[key] = self.root.insert(Node(key, 1))
            else:
                self.root.next.keys.add(key)
                self.nodes[key] = self.root.next
        else:
            cur = self.nodes[key]
            nxt = cur.next
            if nxt is self.root or nxt.count > cur.count + 1:
                self.nodes[key] = cur.insert(Node(key, cur.count + 1))
            else:
                nxt.keys.add(key)
                self.nodes[key] = nxt
            cur.keys.remove(key)
            if len(cur.keys) == 0:
                cur.remove()

    def dec(self, key: str) -> None:
        cur = self.nodes[key]
        if cur.count == 1:  # key 仅出现一次，将其移出 nodes
            del self.nodes[key]
        else:
            pre = cur.prev
            if pre is self.root or pre.count < cur.count - 1:
                self.nodes[key] = cur.prev.insert(Node(key, cur.count - 1))
            else:
                pre.keys.add(key)
                self.nodes[key] = pre
        cur.keys.remove(key)
        if len(cur.keys) == 0:
            cur.remove()

    def getMaxKey(self) -> str:
        return next(iter(self.root.prev.keys)) if self.root.prev is not self.root else ""

    def getMinKey(self) -> str:
        return next(iter(self.root.next.keys)) if self.root.next is not self.root else ""
