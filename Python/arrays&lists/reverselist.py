lista = [10,20,30,40,50]
lista.reverse()
print(lista) #modifies the list , returns the same list

list1 = [10,20,30]
newlist1 = list(reversed(list1))
print(newlist1)

newlist1 = list1[::-1]
print(newlist1)


def reverseList(list):
    start = 0
    end = len(list) - 1 
    while start < end :
        list[start], list[end] = list[end], list[start]
        start = start + 1 
        end = end - 1

listb= [10,76,24,56,64,100,22]
reverseList(listb)
print(listb)

