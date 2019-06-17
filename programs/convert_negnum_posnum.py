# convert negitive to positive
num=[1,-1,2,-3,-3,3,2,1,4,5,6,-2,-3,-4,-5,-7,-9,-2.6,-4.6,5.6,-7.43]
pos_num=[]
for i in num:
    if i>0:
        pos_num.append(i)
    else:
        pos_num.append(i*-1)
print(pos_num)


# convert positive to negitive
num1=[1,-1,2,-3,-3,3,2,1,4,5,6,-2,-3,-4,-5,-7,-9,-2.6,-4.6,5.6,-7.43]
neg_num=[]
for i in num1:
    if i<0:
        neg_num.append(int(i))
    else:
        neg_num.append(int(i)*-1)
print(neg_num)
print(set(neg_num))
print(tuple(neg_num))
print(frozenset(neg_num))
