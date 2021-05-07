# q 
# d={ "b":58,
#     "c":56,
#     "d":40,
#     "e":100,
#     "f":20
# }
# a=[]
# b=[]
# for i in d:
#     a.append(i)
#     b.append(d[i])
# c=[]
# i=0
# while i<len(a):
#     c.append((b[i],a[i]))
#     i+=1
# d={}
# d.update(c)
# list1=[]
# for j in d:
#     list1.append(j)
# max1=max(list1)
# list1.remove(max1)
# max2=max(list1)
# list1.remove(max2)
# max3=max(list1)
# p=[]
# p.append(d[max1])
# p.append(d[max2])
# p.append(d[max3])
# print(p)

#second method
my_dict={'a':50,'b':58,'c':56,'d':40,'e':100,'f':20}
my_list=[]
my_list_key=[]  
for i in range(3):
    max_1=0
    for value in my_dict:  
        if max_1<my_dict[value]:
            max_1=my_dict[value]
            key=value
    my_list.append(max_1)
    my_list_key.append(key)
    my_dict.pop(key)
print(my_list)
print(my_list_key)