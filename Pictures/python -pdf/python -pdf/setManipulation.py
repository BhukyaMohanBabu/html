'''set data manipulation :
predifined class for set is class set
set is unordered 
mutable collection
each object seperated by , 
every object must take in the {}
duplicate object are not allowed
insertion ordered is not maintained 
heterogeneous object are allowed 
method in the set are 
1.copy()
2.clear()
3.pop()
4.remove()
5.update()
6.union()
7.intersection()
8.discard()
9.difference()
10.issuperset()
11.issubset()
12.isdisjoint()
13.add()
'''
set1={1,2,3,4,4,4,5,6,"python","programming"}
set2={1,2,3,4,}
print(type(set2))
#set1.copy()
#set1.clear()
#set1.pop()
#set1.remove("python")
#set1.update({7000})
#set1.add("pyhtonnnnn")
#print(set1.union(set2))
#print(set1.difference(set2))
#print(set1.intersection(set2))
#set1.discard("python")
#print(set1.issuperset(set2))
#print(set1.issubset(set2))
print(set1.isdisjoint(set2))


















