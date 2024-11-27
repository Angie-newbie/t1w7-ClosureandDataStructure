# List - ordered (indexed) collection of items - mutable - can have duplicates

#  Set - Unordered - Not indexed - mutable - no duplicates

names_set = {"john", "Jane", "Stacy", "Mike"}


names_set.add("Mary")
print(names_set)
print(len(names_set))

names_set.remove("john")
print(names_set)

names_set.add("Jane")
print(names_set)


set1 = {1, 2, 3, 4, 5}
set2 = {1, 3, 5, 7, 9}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))

print(set1 - set2)
