#q1
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# l=[]
# for i in keys:
#     for j in values:
#             l.append((i,j))
#             a={}
#             a.update(l)
# print(a)
##second method 
# l=[]
# i=0
# while i<len(keys):
#     l.append((keys[i],values[i]))
#     i+=1
# a={}
# a.update(l)
# print(a)
# q2
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# l={}
# l.update(dict1)
# l.update(dict2)
# print(l)
#q3
# sampleDict = { 
#    "class":{ 
#       "student":{ 
#          "name":"Mike",
#          "marks":{ 
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }
# print(sampleDict["class"]["student"]["marks"]["history"])
#q4
employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}
Dict1= dict.fromkeys(employees, defaults)
print(Dict1)
print(Dict1["Kelly"])

#q5
# sampleDict = { 
#   "name": "Kelly",
#   "age":25, 
#   "salary": 8000, 
#   "city": "New york" }

# keys = ["name", "salary"]     #not done
# for i in keys:
#     dic1={}
#     dic1.update({i:sampleDict[i]})
#     print(dic1)
# l={}
# l.update(dic1)
# print(l)
#q6
# sampleDict = {
#   "name": "Kelly",  #not 
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
  
# }
# keysToRemove = ["name", "salary"]
# # for i in sampleDict:
#     # if "name" and "salary" in sampleDict:
# print()
