# A set is a collection which is unordered, 
# unchangeable*, and unindexed.

new_set = {"DSA", "EDC", "DSD", "MAT", "DSA"}
# Duplicates are not allower in a set
# print(my_set)

my_set = {"DSA", 0, "DSA", True, 45, "EDC"}
# print(set(("DSA", "EDC", "DSD", "MAT", "DSA")))

new_set.remove("EDC")
# print(new_set)

x = {'apple', 'mango', 'banana', 'papaya', 'cherry', 'pineapple'}
print(x)
print(x.pop())

y = {'google', 'microsoft', 'tesla'}

y.update(x)
print(y)

y.clear()
print(y)

