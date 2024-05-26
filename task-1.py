class Node:
    def __init__(self, data=None):
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
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end=" -> ")
            cur_node = cur_node.next
        print("None")

def reverse_linked_list(linked_list):
    prev = None
    current = linked_list.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    linked_list.head = prev

llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
print("Original List:")
llist.print_list()  
reverse_linked_list(llist)
print("Reversed List:")
llist.print_list() 

def merge_sort_linked_list(head):
    if not head or not head.next:
        return head

    def get_middle(head):
        if not head:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def sorted_merge(left, right):
        if not left:
            return right
        if not right:
            return left
        if left.data <= right.data:
            result = left
            result.next = sorted_merge(left.next, right)
        else:
            result = right
            result.next = sorted_merge(left, right.next)
        return result

    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None

    left = merge_sort_linked_list(head)
    right = merge_sort_linked_list(next_to_middle)

    sorted_list = sorted_merge(left, right)
    return sorted_list

def sort_linked_list(linked_list):
    linked_list.head = merge_sort_linked_list(linked_list.head)

llist = LinkedList()
llist.append(3)
llist.append(1)
llist.append(2)
print("Unsorted List:")
llist.print_list() 
sort_linked_list(llist)
print("Sorted List:")
llist.print_list() 

def merge_sorted_linked_lists(list1, list2):
    dummy = Node()
    tail = dummy

    l1, l2 = list1.head, list2.head

    while l1 and l2:
        if l1.data <= l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    else:
        tail.next = l2

    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list

llist1 = LinkedList()
llist1.append(1)
llist1.append(3)
llist1.append(5)
print("First Sorted List:")
llist1.print_list()  

llist2 = LinkedList()
llist2.append(2)
llist2.append(4)
llist2.append(6)
print("Second Sorted List:")
llist2.print_list()

merged_llist = merge_sorted_linked_lists(llist1, llist2)
print("Merged Sorted List:")
merged_llist.print_list() 
