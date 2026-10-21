text = input("Enter a string:")

print("\nIndexing")
print("First character (text[0]:",text[0])
print("Last character (text[0]:",text[-1])
print("\nSlicing:")
print("First 3 characters(text[0:3]):",text[0:3])
print("From 2nd to last(text[1:]):",text[1:])

print("\nModifying:")
#Modifying (Strings are immutable, so we create a new string)
new_text = "X" + text[1:] # Replace first character with 'X'
print("After Replacing first character with "X":",new_text)

print("\nRepeating:")
print("Repeat string 3 times:",text*3)

print("\nConcatenation:")
extra = "Python"
combined = text +" " + extra
print("New Words =",combined)
