fruits = ["apple", "banana", "cherry"]
print("Enumerating fruits:")
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")    

names= ["Prakash", "Ramesh", "Suresh"]
marks = [85, 90, 78]
print("\nZipping names and marks:") 
for name, mark in zip(names, marks):
    print(f"Name: {name}, Mark: {mark}")