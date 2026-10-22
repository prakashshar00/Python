fruits = ['apple','banana','litchi','mango']
print("\nInitital Elements") # ['apple','banana','litchi','mango']

# Adding Elements
# 1. Append() - Add one element at the end
fruits.append("oranges")
print("After append (oranges):",fruits) # ['apple','banana','litchi','mango','oranges']

# 2. insert() - add elements at specific index
fruits.insert(1,"cherry")
print("After append (cherry):",fruits) # ['apple','cheery','banana','litchi','mango','oranges']

# 3. extend() - add multiple elements from another list
fruits.extend(['pine apple','grapes','Avogado','dragon fruits','guava'])
print("After extend",fruits) # ['apple','cheery','banana','litchi','mango','oranges','pine apple','grapes','Avogado','dragon fruits','guava']


#REMOVING ELEMENTS
# 1. remove() - removes the first matching elements by value.
fruits.remove("banana") #  ['apple','cheery','litchi','mango','oranges','pine apple','grapes','Avogado','dragon fruits','guava']

#2. pop() - removes element at index and returns it; default is last element
removed_items = fruits.pop()
print("After pop():",fruits) # ['apple','cheery','litchi','mango','oranges','pine apple','grapes','Avogado','dragon fruits']

removed_item_at_index = fruits.pop(2) # Removes the element at index 2
print("after pop(2)",fruits) # ['apple','cheery','mango','oranges','pine apple','grapes','Avogado','dragon fruits']
print("Removed item is ", removed_item_at_index)

#3. clear() - Removes all the elements from the list
fruits.clear() 
print("\nAfter clear():",fruits)
