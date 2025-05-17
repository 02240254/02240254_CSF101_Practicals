class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def search(self, data):
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def remove_nth_from_end(self, n):
        dummy = Node(0)
        dummy.next = self.head
        fast = slow = dummy
        for _ in range(n):
            if fast.next is None:
                return  # n is larger than list size
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        self.head = dummy.next

    def merge_sorted(self, other):
        dummy = Node(0)
        tail = dummy
        l1 = self.head
        l2 = other.head
        while l1 and l2:
            if l1.data <= l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 or l2
        self.head = dummy.next

    def find_middle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if slow:
            print("Middle element:", slow.data)
        else:
            print("The list is empty.")

    def has_cycle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                print("Cycle detected!")
                return True
        print("No cycle.")
        return False

    def remove_duplicates(self):
        seen = set()
        current = self.head
        prev = None
        while current:
            if current.data in seen:
                prev.next = current.next
            else:
                seen.add(current.data)
                prev = current
            current = current.next


# Sample test
if __name__ == "__main__":
    ll = LinkedList()
    for val in [1, 2, 3, 4, 5]:
        ll.append(val)
    print("Original list:")
    ll.display()

    print("\nAfter inserting 10 at position 2:")
    ll.insert(10, 2)
    ll.display()

    print("\nAfter deleting 3:")
    ll.delete(3)
    ll.display()

    print("\nSearch for 4:", ll.search(4))
    print("Search for 99:", ll.search(99))

    print("\nReversed list:")
    ll.reverse()
    ll.display()

    print("\nRemove 2nd node from end:")
    ll.remove_nth_from_end(2)
    ll.display()

    print("\nFind middle element:")
    ll.find_middle()

    print("\nCheck for cycle:")
    ll.has_cycle()

    print("\nAdd duplicates and remove them:")
    ll.append(10)
    ll.append(1)
    ll.append(4)
    ll.display()
    ll.remove_duplicates()
    ll.display()

    print("\nMerge with another sorted list:")
    ll2 = LinkedList()
    for val in [0, 6, 7]:
        ll2.append(val)
    ll.merge_sorted(ll2)
    ll.display()
