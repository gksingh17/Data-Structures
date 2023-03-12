list = [10,20,30]
#yes
list1 = [10,20,20,30]
#yes
list2 = [10,5,2]
#no
list3 = [10]
#yes
list4 = []
#no
list5 =  [10,20,30,15,40]

def issorted(list):
    if len(list) <= 1:
        return True 
    else:
        for i in range(len(list)):
            if i > i+1:
                break #need to add break else it will hold true for further elements
            return False    
        return True
            
print(issorted(list5))

def whileSorted(list):
    i = 1
    while i < len(list):
        if list[i] < list[i-1]:
            return False
        i = i + 1
    return True

if whileSorted(list5):
    print("yes")
else: 
    print("No")
        
def methodIsSorted(list):
    sortedList = sorted(list) #sorted method, creates a new list 
    if sortedList == list:
        return True 
    else:
        return False         #this is not efficent than previous methods
    
if methodIsSorted(list5):
    print("yes")
else: 
    print("No")
