import task1_1
def sum(lst1, lst2):
    sum_list = LinkList() 
    #max_len = max(lst1.len(), lst2.len())
    #min_len = min(lst1.len(), lst2.len())
    len_flag = lst1.len() > lst2.len()
    buf_lst1 = lst1.first
    buf_lst2 = lst2.first
    flag = 0
    while buf_lst1 is not None and buf_lst2 is not None:
        sum_list.pushhead((buf_lst1.value + buf_lst2.value + flag) % 10)
        if ((buf_lst1.value + buf_lst2.value + flag) // 10) != 0:
            flag = 1
        else:
            flag = 0
        buf_lst1 = buf_lst1.next
        buf_lst2 = buf_lst2.next
    print(111)
    if len_flag:
        while buf_lst1 is not None:
            sum_list.pushhead((buf_lst1.value + flag) % 10)
            if ((buf_lst1.value + flag) // 10) != 0:
                flag = 1
            else:
                flag = 0
            buf_lst1 = buf_lst1.next
    else:
        while buf_lst2 is not None:
            sum_list.pushhead((buf_lst2.value + flag) % 10)
            if ((buf_lst2.value + flag) // 10) != 0:
                flag = 1
            else:
                flag = 0
            buf_lst2 = buf_lst2.next
    if flag == 1:
        sum_list.pushhead(flag)
    return sum_list
