list = [10, 20, 30, 40, 50]
#index [0,  1,  2,   3,  4]
#      [-5, -4, -3, -2, -1]

#list[start:stop:step] -> start is inclusive, stop is exclusive
print(list[0:5:2]) #0 - > 10(inclusive), increment by 2 so 30 , increment by 2 so 50
# note the last element is indexed at 4 so 5th element is exclusive if it did exist. 

print(list[:4]) #start is 0 by default and step is 1 by default
print(list[2:]) #when stop not included len(list) is default, so 5

print(list[1:4]) #start 1 -> 20, stop 4 -> 40
print(list[4:1:-1]) #start -> 50 , step -1 -> reverse, stop -> 30 

print(list[-1:- 6:-1]) #start -> 50, step -1 -> reverse, stop -> 10
print(list[::-1]) #reverse of a list 

print(list[:]) #returns the whole list


list1 = [10, 20, 30]
list2 = list1[:]  # copies element in list 2

tuple1 = (10, 20, 30)
tuple2 = tuple1[:]

string ="green"
string1 = string[:]

print(list1 in list2)
print(tuple1 in tuple2)
print(string1 in string)

