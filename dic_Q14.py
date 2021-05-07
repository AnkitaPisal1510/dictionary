#q14
dic={'bjendar':45,'deepak':60,'param':20,'anjali':30,'roshani':50}
dic2={} 
for i in dic:
    s=dic[i]
    for j in dic:
        a=dic[j]
        if s<a:
            dic2[j]=a
for i in dic:
    s=dic[i]
    for j in dic:
        a=dic[j]
        if s>a:
            dic2[j]=a
print(dic2)