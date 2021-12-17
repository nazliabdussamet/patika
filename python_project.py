#First question:
#In this question the given list will be flatten.

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

#Second Question:
#In this question the given list will be reversed.

def reverselist(mylist):
    reversedlist = []
    
    for i in range(len(mylist)):
        reversedlist.append(mylist[-i-1])
    
    i = 0
    for item in reversedlist:
        if type(item) == list:
            reversedlist[i] = reverselist(item)
        i += 1
    
    return reversedlist
    

mylist = [] #Give the list
reversedlist = []

for i in range(len(mylist)):
    reversedlist.append(mylist[-i-1])

i = 0
for item in reversedlist:
    if type(item) == list:
        reversedlist[i] = reverselist(item)
    i += 1

print(reversedlist)
