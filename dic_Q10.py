#
#q10
d={
    "alex":["sub1","sub2","sub3"],
    "david":["sub1","sub2"]
}
# l=[]
# for i in d:
#     # print(y[i])
#     # print(len(y[i]))
#     j=len(d[i])
#     l.append(j)
# print(sum(l))
#second method
list1=[]
for i in d.values():
    for j in i:
        list1.append(j)
print(len(list1))
print(list1)