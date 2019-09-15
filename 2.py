class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class LinkList:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    def __str__(self):
        if self.first != None:
            current = self.first
            out = 'LinkedList (' + str(current.value) 
            while current.next != None:
                current = current.next
                out += '->'  + str(current.value)  
            return out + ')'
        return 'LinkedList []'

    def clear(self):
        self.__init__()

    def pushhead(self, x):
        self.length += 1
        if self.first == None:
            self.first = self.last = Node(x, None)
        else:
            self.first = Node(x, self.first)

    def pushback(self,x):
        self.length += 1
        if self.first == None:
            self.first = self.last = Node(x, None)
        else:
            self.last.next = self.last = Node(x, None)

    def pushanywhere(self, x, number):
        self.length += 1
        if self.first == None:
            self.first = self.last = Node(x, None)
            return
        if number == 0:
            self.first = Node(x, self.first)
            return
        cycle_num = 1
        buf = self.first
        while buf != None:
            if cycle_num == number:
                buf.next = Node(x, buf.next)
                if buf.next == None:
                    self.last = buf.next
                break
            cycle_num += 1
            buf = buf.next

    def find(self, num):    
        buf = self.first
        while buf != None:
            if buf.value == num:
                return buf
            else: 
                if buf.next != None:
                    buf = buf.next
                else:
                    break
        buf = None
        return buf

    def delete(self, x):
        if self.first == None:
            return
        current = self.first
        prev = None
        cycle_num = 0
        self.length -= 1
        if x == 0:
          self.first = self.first.next
          return
        while current != None and cycle_num != x:
            prev = current
            current = current.next
            cycle_num += 1
        prev.next = current.next    

    def len(self):
        return self.length

def num_to_list(number): #head - end
    num_list = LinkList()
    num_list.pushback(number % 10)
    number //= 10
    while number != 0:
        num_list.pushback(number % 10)
        number //= 10   
    return num_list

def sum(lst1, lst2):
    sum_list = LinkList() 
    max_len = max(lst1.len(), lst2.len())
    min_len = min(lst1.len(), lst2.len())
    len_flag = lst1.len() > lst2.len()
    buf_lst1 = lst1.first
    buf_lst2 = lst2.first
    flag = 0
    while buf_lst1 != None and buf_lst2 != None:
        sum_list.pushhead((buf_lst1.value + buf_lst2.value + flag) % 10)
        if ((buf_lst1.value + buf_lst2.value + flag) // 10) != 0:
            flag = 1
        else:
            flag = 0
        buf_lst1 = buf_lst1.next
        buf_lst2 = buf_lst2.next
    print(111)
    if len_flag:
        while buf_lst1 != None:
            sum_list.pushhead((buf_lst1.value + flag) % 10)
            if ((buf_lst1.value + flag) // 10) != 0:
                flag = 1
            else:
                flag = 0
            buf_lst1 = buf_lst1.next
    else:
        while buf_lst2 != None:
            sum_list.pushhead((buf_lst2.value + flag) % 10)
            if ((buf_lst2.value + flag) // 10) != 0:
                flag = 1
            else:
                flag = 0
            buf_lst2 = buf_lst2.next
    if flag == 1:
        sum_list.pushhead(flag)
    return sum_list



if __name__ == "__main__":

    L =   num_to_list(1)
    L2 = num_to_list(9999)
    print(sum(L, L2))