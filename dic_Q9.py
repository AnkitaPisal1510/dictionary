# q9
a="MISSISSIPI"
h=[]
x={}
for i in a:
    h.append(i)
    s=h.count(i)
    x.update({i:s})
print(x)