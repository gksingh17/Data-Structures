list = [10, 5, 20, 8]
print(max(list))

def largestelement(list):
    for i in list:
        for j in list:
            if i > j:

                break
        else:
            return i
    return None

#time complexity is O(n^2)


def getMax(list):
    if not list:
        return None
    else:
        result = list[0]
        for i in range(1,len(list)):
            if list[i] > result:
                result=list[i]
        return result
    
print(getMax(list = [10, 5, 20, 8]))

#O(n)