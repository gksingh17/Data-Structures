list = [10, 20, 30, 40]

def avg(list):
    sum = 0 
    for i in list:
        sum = sum + i #itertate though all the elements and add i 
    n = len(list)
    return sum/n 

print(avg(list)) 

def avglib(list):
    return sum(list)/len(list) #using library functions 

print(avglib(list))

