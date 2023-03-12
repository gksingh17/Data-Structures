def rotateByOne(list):
    n = len(list)
    x = list[0] #the first element will be overridden 
    for i in range(1,n):
        list[i-1] = list[i]
    list[n-1] = x #last element
    return list

list = [10,20,30,40]
print(rotateByOne(list))

list1 = [10,20,30,40]
listresult = list1[1:] + list1[0:1] 
print(listresult)

list2 = [10,20,30,40]
list2.append(list2.pop(0))
print(list2)


testlist = [1, 2, 3, 4, 5]
# [2,3,4,1] -> [3,4,1,2] 
#d = 3 - > []
def rotateBySteps(list,d):
    d = d % len(list)
    list[:] = list[-d:] + list[:-d]
    return list 

print(rotateBySteps(testlist,2))

   

    



