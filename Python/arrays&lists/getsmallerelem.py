list = [8, 100, 20, 40, 3, 7]
x = 10 
#output : [8, 3, 7]

list1 = [100, 20, 40, 60, 80, 200]
x = 60
#output : [20, 40]


def getsmaller(list,x):
    smaller = []
    for i in list:
        if i < x : 
            smaller.append(i)
    return smaller 

print(getsmaller(list1,x=60))