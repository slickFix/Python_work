class LinkedList:

    def __init__(self):
        self.head = None

    class Node:

        def __init__(self, data):
            self.data = data
            self.next_node = None

    def swapNodes(self,x,y):

        # if x and y are same return
        if x == y:
            return

        prevx = None
        currx = self.head

        while currx!=None and currx.data != x:
            prevx = currx
            currx = currx.next_node

        prevy = None
        curry = self.head

        while curry!=None and curry.data !=y:
            prevy = curry
            curry = curry.next_node

        # If either x or y is not present, nothing to do
        if currx == None or curry == None:
            return
            # If x is not head of linked list
        if prevx != None:
            prevx.next_node = curry
        else:  # make y the new head
            self.head = curry

            # If y is not head of linked list
        if prevy != None:
            prevy.next_node = currx
        else:  # make x the new head
            self.head = currx

            # Swap next pointers
        temp = currx.next_node
        currx.next_node = curry.next_node
        curry.next_node = temp

    # adds node to the begining of the linked list
    def push(self,data):

        new_node = self.Node(data)

        new_node.next_node = self.head

        self.head = new_node

    def reverse_list(self):

        if self.head is None:
            return None

        prev = None
        curr = self.head
        next_node = None

        while curr is not None:
            next = curr.next_node
            curr.next_node = prev
            prev = curr
            curr = next

        self.head = prev

    def printList(self):

        curr_node = self.head

        while curr_node is not None:
            print(curr_node.data ,end= ' ')
            curr_node = curr_node.next_node


if __name__ == '__main__':

    ll = LinkedList()

    for i in range(15):
        ll.push(i)

    print('ll before swap nodes being called ')
    ll.printList()

    ll.reverse_list()

    print()
    print('ll after reversal !!')
    ll.printList()
