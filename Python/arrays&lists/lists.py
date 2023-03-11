#dynamic size, allows items of different types

listname = [1, 2, 3, 4]
        #   0  1  2  3
        #  -4 -3 -2  -1
print("append")
listname.append(5) #adding element at the end 
print(listname)

print("insert")
listname.insert(0, 0) #insert element at given index
print(listname)

print("In Function")
print(4 in listname) #checks if element present in list 

print("Count")
print(listname.count(3)) 
print("Index")
print(listname.index(1))

print("remove")
listname.remove(1) #removes given value from the list
print(listname)

print("pop")
print(listname.pop()) #removes the last value and returns that value
#index can be provided to pop function 

print("del")
del listname[2]
print(listname)

print("max value")
print(max(listname)) #max value

print("min value")
print(min(listname)) #min value

print("sum of list")
print(sum(listname)) 

print("reverse")
listname.reverse()
print(listname)

print("sort")
listname.sort()
print(listname)

#works when list is of one type for some of the functions 

#lists uses random access, cache friendly 
#lists are based on arrays 
#insertions, deletions and search are slower 
#ex: to insert and element in the begining , all elements needs to be shifted


#Time Complexities 
#insert - O(n)
#append - O(1)
#pop last - O(1)
#copy - O(n) 
#get item -   O(1)
my_list = ['String', 1, 3.5, 100, True]
print(len(my_list)) #length 

print(my_list[0]) #accessing list 

#slicing and indexing 
#[start:end:step] #end is not included  

print(my_list[1:])




