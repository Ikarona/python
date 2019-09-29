dic = {}
while 1:
    string = input().split()
    if string == []:
        break
    for i in string:
        if dic.get(i) == None:
            dic[i] = 0
        else:
            dic[i] += 1
    break
list_sort = list(dic.items())
list_sort.sort(key = lambda i: i[1], reverse = True)
if list_sort[0][1] == list_sort[1][1]:
    print("---")
else:
    print(list_sort[0][0])