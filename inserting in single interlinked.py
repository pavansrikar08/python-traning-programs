class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def iterate(head):
    temp = head
    while temp is not None:
        print(temp.val, end=" ")
        temp = temp.next
    print()


def insert(idx, newnode, head):
    if idx == 0:
        newnode.next = head
        return newnode

    temp = head
    count = 0

    while temp is not None and count < idx - 1:
        temp = temp.next
        count += 1

    if temp is None:
        print("Index out of range")
        return head

    newnode.next = temp.next
    temp.next = newnode
    return head


head = Node(5)
head.next = Node(10)
head.next.next = Node(4)

print("Original list:")
iterate(head)

new_node = Node(7)
head = insert(1, new_node, head)

print("After insertion:")
iterate(head)
