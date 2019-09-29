class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkList:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    def __str__(self):
        if self.first is not None:
            current = self.first
            out = 'LinkedList (' + str(current.value)
            while current.next is not None:
                current = current.next
                out += '->'  + str(current.value)
            return out + ')'
        return 'LinkedList []'

    def clear(self):
        self.__init__()

    def pushhead(self, x):
        self.length += 1
        if self.first is None:
            self.first = self.last = Node(x, None)
        else:
            self.first = Node(x, self.first)

    def pushback(self,x):
        self.length += 1
        if self.first is None:
            self.first = self.last = Node(x, None)
        else:
            self.last.next = self.last = Node(x, None)
            
    def pushanywhere(self, x, number):
        self.length += 1
        if self.first is None:
            self.first = self.last = Node(x, None)
            return
        if number == 0:
            self.first = Node(x, self.first)
            return
        cycle_num = 1
        buf = self.first
        while buf is not None:
            if cycle_num == number:
                buf.next = Node(x, buf.next)
                if buf.next is None:
                    self.last = buf.next
                break
            cycle_num += 1
            buf = buf.next

    def find(self, num):
        buf = self.first
        while buf is not None:
            if buf.value == num:
                return buf
            else:
                if buf.next is not None:
                    buf = buf.next
                else:
                    break
        buf = None
        return buf

    def delete(self, x):
        if self.first is None:
            return
        current = self.first
        prev = None
        cycle_num = 0
        self.length -= 1
        if x == 0:
            self.first = self.first.next
            return
        while current is not None and cycle_num != x:
            prev = current
            current = current.next
            cycle_num += 1
        prev.next = current.next

    def len(self):
        return self.length

def num_to_list(number): #head - beginning
    num_list = LinkList()
    num_list.pushhead(number % 10)
    number //= 10
    while number != 0:
        num_list.pushhead(number % 10)
        number //= 10
    return num_list
