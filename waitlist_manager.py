# Create a Node class to represent each customer in the waitlist
class Node:
    def __init__(self, name):
        self.name = name
        self.next = None


# Create a LinkedList class to manage the waitlist
class LinkedList:
    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''
    def __init__(self):
        self.head = None

    def add_front(self, name):
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node

    def add_end(self, name):
        new_node = Node(name)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def remove(self, name):
        # Empty list
        if self.head is None:
            print(f'"{name}" was not found in the waitlist.')
            return

        # Removing the head
        if self.head.name == name:
            self.head = self.head.next
            print(f'Removed "{name}" from the waitlist.')
            return

        # Search the rest of the list
        current = self.head
        while current.next is not None:
            if current.next.name == name:
                current.next = current.next.next
                print(f'Removed "{name}" from the waitlist.')
                return
            current = current.next

        print(f'"{name}" was not found in the waitlist.')

    def print_list(self):
        if self.head is None:
            print("The waitlist is empty.")
            return
        current = self.head
        while current is not None:
            print(current.name)
            current = current.next


def waitlist_generator():
    # Create a new linked list instance
    waitlist = LinkedList()
    
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == "1":
            name = input("Enter customer name to add to front: ")
            waitlist.add_front(name)
            print(f'Added "{name}" to the front of the waitlist.')

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            waitlist.add_end(name)
            print(f'Added "{name}" to the end of the waitlist.')

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            waitlist.remove(name)

        elif choice == "4":
            print("Current waitlist:")
            waitlist.print_list()

        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1-5.")


# Call the waitlist_generator function to start the program
waitlist_generator()


'''
Design Memo (≈250 words)

How the list works:
My waitlist is a singly linked list. Each customer is stored in a Node object that holds two pieces of data: the customer's name and a reference (next) to the following node. The LinkedList class only keeps track of the very first node (head). All other nodes are reached by following the chain of next pointers.

Role of the head:
The head is the entry point into the entire list. Every operation starts from the head:
- add_front simply makes the new node the new head.
- add_end walks from the head until it finds the last node (the one whose next is None) and attaches the new node there.
- remove also starts at the head, checking whether the head itself needs to be removed or walking further to find the matching name.
- print_list begins at the head and follows next pointers until it reaches the end.

When a real engineer might need a custom list like this:
Python's built-in list is excellent for most everyday work, but a custom linked list becomes useful when:
- You need frequent insertions or deletions at the front (O(1) with a linked list vs O(n) with a dynamic array).
- You are working in a memory-constrained environment or with very large data where you want to avoid the occasional expensive resizing of a dynamic array.
- You need to implement more advanced structures (queues, stacks, adjacency lists for graphs, etc.) or when teaching/understanding the fundamentals of data structures.
- You are interfacing with systems or languages that expose linked-list style APIs (certain C libraries, database cursors, etc.).

In short, a hand-rolled linked list gives precise control over memory layout and insertion/deletion cost that the more general-purpose list cannot always provide.
'''