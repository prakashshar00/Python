my_set = {1,2,3,4}
print("Initial set:", my_set)

# Adding elements to the set
my_set.add(5)
print("Set after adding 5:", my_set)

my_set.update([6, 7, 8])
print("Set after adding multiple elements:", my_set)

# Removing elements from the set
my_set.remove(4)
print("Set after removing 4:", my_set)

my_set.discard(5)
print("Set after discarding 5:", my_set)
# no error if elements is not found

removed = my_set.pop() # it removes the first element
print("Set after popping an element:", my_set)
print("Removed element:", removed)

my_set.clear()
print("Set after clearing all elements:", my_set)