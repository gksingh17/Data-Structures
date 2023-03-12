list = [5, 20, 12, 10, 20, 10, 12] #20 
list1 = [20,10,20,12] #12
list2 = [10,10,10] #none

def secondLargest(list):
    if len(list) <= 1:
        return None
    largest = max(list)
    seclargest = None
    for i in list:
        if i != largest:
            if seclargest == None:
                seclargest = i #initiates the first element in the list to compare with the largest
            else:
                seclargest = max(seclargest, i) 
    return seclargest

def getSecMax(list):
        if len(list) <= 1:
             return None
        lar = list[0]; slar = None

        for x in list[1:]:
             if x > lar: #if 20 is greater than 5 (current element greater than lar =list[0])
                  slar = lar # slar = 5 , lar = 5 
                  lar = x #lar = 20 
             elif x != lar:
                  if slar == None or slar < x:
                       slar = x
        return slar 


                       
                  


