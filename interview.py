# dic1={'a':100,'b':200,'c':300}
# dic2={'a':300,'b':200,'c':400}
# k=[]
# j1=[]
# for index in (dic1):
#     for j in dic2:
#         if index==j:
#             a=((index,dic1[index]+dic2[j])) 
#             k.append(a)
#         if index!=j:
#                 j1.append(a)
                
# s={}
# s.update(k) 
# s.update(j1)       
# print(s)
#     #     # if dic1.keys()==dic2.keys():
#         #     x=dic1[index]+dic2[j]
#         # print(x)

#13 hamara max hai max tak kitane elements list mai nahi hai vo dikhata hai
a=[1,13,4,2,6]
count=0
s=min(a)
while s<max(a):
    if s not in a:
        count+=1
    s+=1
print(count)

#short
# a=[1,2,93,34,5]
# b=[]
# i=0
# while i<len(a):
#     c=max(a)
#     a.remove(c)
#     b.append(c)
# print(b)

#split
a="my name is ankita"
s=""
b=[]
for i in a:
    if i==" ":
        b.append(s)
        s=""
    else:
        s+=i
if s:
    b.append(s)
print(b)

#q.my name is swati
#op.My Name Is swati
a="my name is swati"
