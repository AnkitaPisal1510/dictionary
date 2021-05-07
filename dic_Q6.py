#
#q6
d={
    "ball":"red",
    "bat":4,
    "wickets":6,
    "ball":"green",
    "bat":3

}
s={}
print(d)
for i in d:
    s.update({i:d[i]})
print(s)
