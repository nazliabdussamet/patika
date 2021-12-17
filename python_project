#First question:

def flatten_list(mylist, sublist):
    for i in sublist:
        if type(i) == list:
            flatten_list(mylist,i)
        else:
            mylist.append(i)

mylist = [] #Give the list
myflattenlist = []

k = True
i = 0

for i in mylist:
    if type(i) == list:
        flatten_list(myflattenlist, i)
    else:
        myflattenlist.append(i)

print(myflattenlist)
