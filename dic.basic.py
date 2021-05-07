# city={
#     "newyork":132433,
#     "losangeles":1233454,
#     "toronto":35224343,
#     "chicago":12435435,
#     "houston":2144234,
#     "montreal":42356725,
#     "calgary":31245322,
#     "vancouver":23435678,
#     "boston":2454325
# }
# print(city["newyork"])
# print(city)
# print(type(city))

# s=dict(name="ravina",age=20)
# print(s)
# dic= {
#     1: 'navgurukul',
#     2: 'in',
#     3:{
#         "A":'WELCOME',
#         'B':'TO',
#         'C':'PUNE'
#     }
# }
# print(dic)
#accessing elements from a dictionary
# p={
#     'name':'jack',
#     'age':20,
#     'gender':"male",
#     4:"organisation"
# }
# result = p['age']
# x=p.get('gender')
# print(p[4])
# print(x)
# print(result)

#adding elements to a list
# dic={
#     'name':'ankita',
#     'age':16
# }
# dic['student']={'org':'navgurukul','place':'pune'}
# print(dic)

#loop through dictionary
#here brand ,model,year=key this is also called index values
# dic={'brand':'suzuki','model':'dzire','year':2020}
# for x,y in dic.items():
#     print(x,y)
# dic['brand']="kl"
# print(dic)

#
# dic={'name':'alfaj','age':23}
# print(dic)
# print(dic['name'])
# print(dic['age'])
# dic["collage"]="vvk"
# print(dic)

#use of get
# p={
#     'name':'abhishek',
#     "age":20,"study":"bsc physics",
#     "living":'guwahati',
#     5:{'current':"single but committed and also hope is there","wish":"can't express",
#         'affers':'no he is loyal with his love'}
# }
# print(p[5])
# r=p[5]["affers"]
# print(r)
# j=p.get("name")
# print(j)
# p['nature']="he is not talking with girls except someone"
# print(p)
# p[4]="good looking"
# print(p)
# p[5]["wish"]="meet someone"
# print(p)
# j=p.copy()
# print(j)
# p.pop("living")
# print(p)
# del p["age"]
# print(p)
# p.popitem()
# print(p)
#popitem karenge to last wala key or uski value chali jayegi
# a={"name":"ankita","age":16,
# "study":{"now ":"deploma of computer enginering","educational":11}}
# print(a)
# print(a["study"])
# print("keys",a.keys())#jab bhi ham keys ya fir values nikalte hai to output list mai aata hai
# print("values",a.values())
# q=a["dream"]={"neavy officer"}
# print("new",a)



# ##accesing elements 
# 1
#  y={
#     "name":"sanjana",
#     "age":23,
#     "kl":"rahul"
# }
# print(y["age"])
# #2
# print(y.get('age'))
# print(y.keys()) 
# #or
# p=y.keys()
# print(p)
# y["std"]=11
# print(y)
# print(y.values())
# print(y.items())
# y.update({"age":13})
# print(y)
# y.pop("age")
# print(y)
##last key and value
# y.popitem()
# print(y) 
# del y["name"]
# print(y)
# #clear=none
# print(y.clear())

