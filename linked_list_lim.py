# Assessment 3.2 - Linked List (dynamic version of LinkedListLIM)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def show(head):
    items = []
    current = head
    while current is not None:
        items.append(current.data)
        current = current.next
    print(" -> ".join(items + ["NULL"]))


def main():
    name = input("Enter your last name: ").strip().upper() or "LIM"
    head = None

    # ADD each letter at the tail
    for letter in name:
        new_node = Node(letter)
        if head is None:
            head = new_node
        else:
            current = head
            while current.next is not None:
                current = current.next
            current.next = new_node
        print("Added", letter)
        show(head)

    # REMOVE each letter from the head
    while head is not None:
        print("Removed", head.data)
        head = head.next
        show(head)

    print("Linked list is empty")


if __name__ == "__main__":
    main()
