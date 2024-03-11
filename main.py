class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self):
        return str(self.data)

a = int(5)

node1 = Node(5)
node2 = Node(2)

print(node2)

c = list(range(100))
print(type(c))
print(type(a))
print(type(node1))

