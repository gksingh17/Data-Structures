list1 = [x for x in range(11) if x%2 == 0] #append x in range (0,11) for even numbers
list2 = [x for x in range(11) if x%2 != 0] #append x in range (0,11) for odd numbers

print(list1)
print(list2)

def getsmaller(list, x):
    return [i for i in list if i < x ]

print(getsmaller(list=[1,3,5,6,11],x=5))

def getevenodd(list):
    even = [i for i in list if i%2==0]
    odd = [i  for i in list if i%2!=0]
    return even, odd

even, odd = getevenodd(list=[1,4,7,37,52,61,77,90])
print(even)
print(odd)

string = "floccinaucinihilipilification"
l1 = [x for x in string if x in "aeiou"]
print(l1)

l2 = ["flocci", "nauci", "nihili", "pilification"]
l3 = [x for x in l2 if x.startswith("p")]
print(l3)

l4 = [x*2 for x in range(6)]
print(l4)

l5 = [x.upper() for x in l2 if x.startswith("n")]
print(l5)


#dictonary comprehesion 
list = [1,2,3,4,5]
d1 = {x:x**3 for x in list}
print(d1)

d2 = {x:f"ID{x}" for x in range(5)}
print(d2)

list3 = [3,4,5]
list4 = ["hello", "hi", "hey"]
d3 = {list3[i]:list4[i] for i in range(len(list4)) }
print(d3)

#better way to create to create dic from two lists 
d4 = dict(zip(list3,list4)) #mappings of elements 
print(d4)

#inverted dic
d5 = {v:k for (k,v) in d4.items()}
print(d5)
