a=[12,14,20,19,27,19]
#string cheak
print("java" in a)  #true
print("jas" in a)   #false
print("python" not in a)    #false
print("jas" not in a)   #true

print(a*3)  #print 3 times\
print(len(a))   #lenth print

a.insert(2,10)     #new value add in 2nd index
print(a)

a.remove(27)  #remove python
print(a)

a.sort()    #sorting
print(a)

b=a.copy()  #copy in b
print(b)

a.clear()   #clear
print(a)

pos=b.index(19) #index for 19
print(pos)

pos=b.count(19) #count for how many time 19 in this arry
print(pos)