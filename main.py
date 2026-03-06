sample_list = [1,1,2,3,3,4,5,6,1,3,3,4,]
print(type(sample_list))
print(sample_list)

sample_set = set(sample_list)
print(type(sample_set))
print(sample_set)

if 100 in sample_set:
    print("yes")
else:
    print("no")

mySet = set([])
mySet.add(70)
mySet.add(32)
mySet.add(92)
mySet.add(56)
mySet.add(29)
print(mySet)
mySet.remove(92)
print(mySet)

#remove will throw error, if the element is not present in the set
#mySet.remove(30)
print(mySet)

#Discard will not throw error, even if the number does not exist in the set
mySet.discard(30)
print(mySet)

#Set Operations 
# 1) Union
# 2) Intersection
# 3) Diffrence 
# 4) Symmetic diffrence

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(a.union(b))
print(a | b)

print(a.intersection(b))
print(a & b)

print (a.difference(b))
print(a - b)
print (b.difference(a))
print(b - a)
print(a.symmetric_difference(b))
print(a ^ b)

