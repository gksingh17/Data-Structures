list = [10, 41, 30, 15, 80]
#even = [10, 30, 80]
#odd = [41, 15]


def evenodd(list):
    even =[]
    odd=[]
    for i in list: 
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even, odd    # this becomes a tuple so you need to unpack it 

#unpacking 
even, odd = evenodd(list)
print(even)
print(odd)