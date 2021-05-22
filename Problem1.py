
#sum of nodes whose sum is not zero

class Node(object):
    def __init__(self,data):
        self.data = data # contains the data
        self.next = None # contains the reference to the next node


class LinkedList:
    def __init__(self):
        self.cur_node = None
        self.head = self.tail = None

    def add_node(self, data):
        tempNode = Node(data)
        tempNode.next = self.cur_node
        self.cur_node = tempNode

    def list_print(self):
        node = self.cur_node
        while node:
            print(node.data)
            node = node.next
    def add(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
    def listprint(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next



ll = LinkedList()
ll.add(4)
ll.add(6)
ll.add(-10)
ll.add(8)
ll.add(9)
ll.add(10)
ll.add(-19)
ll.add(10)
ll.add(-18)
ll.add(20)
ll.add(25)


#ll.listprint()


def calculate(ll):
    head = ll.head
    stack = []
    while head:
        value = head.data
        if value < 0:
            while len(stack) != 0:
                sum = stack.pop() + value
                if sum == 0:
                    break
        else:
            stack.append(value)
        head = head.next
    print(stack)



calculate(ll)