def mergesort(list):
    if len(list)==1:
        return list
    else:
        list1=mergesort(list[0:len(list)/2])
        list2=mergesort(list[len(list)/2:len(list)])
        return merge(list1, list2)

def merge(list1, list2):
    newlist = []
    while list1 and list2:
        if list1[0]<list2[0]:
            newlist.append(list1[0])
            del(list1[0])
        else:
            newlist.append(list2[0])
            del(list2[0])
    if list1:
        newlist=newlist+list1
    else:
        newlist=newlist+list2
    return newlist

