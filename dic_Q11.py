#q11
my={
    "a":50,
    "b":58,
    "c":56,
    "d":40,
    "e":100,
    "f":20,
    "g":320,
    "s":1000,
    "e":1200
}
# del my["a"]
# print(my)
# my.pop("b")
# print(my)

# j=[]
# for i in my:
#     j.append(my[i])
# # print(j)
# k=max(j)
# # print("first max:",k)
# j.remove(k)
# a=max(j)
# # print("second max:",a)
# j.remove(a)
# g=max(j)
# # print("third max:",g)
# q=[]
# q.append(g)
# q.append(a)
# q.append(k)
# print(q)

# # a=[]
# # for j in my.values():
# #     a.append(j)
# # b=[]
# # i=0
# # while i<len(a):
# #     c=max(a)
#     a.remove(c)
#     b.append(c)
#     i+=1
# print(b)

a=[]
for i in my:
    a.append(my[i])
i=0
while i<len(a):
    j=0
    while j<len(a)-1:
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
        j=j+1
    i+=1
k=a[-3:]
print(k)