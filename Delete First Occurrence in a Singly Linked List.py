
class Node:
    def __init__(self, data):
        self.data = data      
        self.next = None      

class LinkedList:
    def __init__(self):
        self.head = None      

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def delete_first(self, value):
        temp = self.head

        if temp is None:
            print("List is empty")
            return

        if temp.data == value:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != value:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Value not found in the list")
            return

        prev.next = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


ll = LinkedList()


ll.append(10)
ll.append(20)
ll.append(30)
ll.append(20)
ll.append(40)

print("Original List:")
ll.display()


ll.delete_first(20)

print("Updated List after deleting first occurrence:")
ll.display()
