def removeDup(list):
    result =[]
    for i in list:
        if i not in result:
            result.append(i)
    return result

list1 = [10,20,20,30,30,30,40,50,50]
print(removeDup(list1))


def remDup (arr,n): #sorted array 
    temp = [0]*n 
    temp[0] = arr[0] #first element is distinct so copy 
    result = 1
    for i in range(1,n):
        if temp[result-1] != arr[i]:
            temp[result] = arr[i]
            result += 1 
    for i in range(0,result):
        arr[i] = temp[i]
    return result

def remDup(arr,n):
    res = 1 
    for i in range(1,n):
        if(arr[res-1]) != arr[i]:
            arr[res]= arr[i]
            res += 1       
    return res    


