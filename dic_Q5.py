# q5
# list1=['one','two','three','four','five']
# list2=[1,2,3,4,5]
# # k=[]
# # i=0
# # while i<len(list1):
# #     k.append([list1[i],list2[i]])
# #     i+=1
# # l={}
# # l.update(k)
# # print(l)
# # second method
# k={}
# for i in range(len(list1)):
#     k.update({list1[i]:list2[i]})
# print(k)

d=["keemaya","17","pune","maharastra"]
s=["name","age","live","k"]
k={}
for i in range(len(s)):
    k.update({s[i]:d[i]})
print(k)
