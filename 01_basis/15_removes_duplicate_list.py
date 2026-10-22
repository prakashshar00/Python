my_list = [1,2,3,4,5,6]
unique_list = list(set(my_list))
print("original list:",my_list)
print("list after removing duplicates (order not guranted):",unique_list)

my_list = [1,2,3,4,5,6,7,8,9]
unique_list =[]
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)
print("original list:",my_list)
print("list after removing duplicates (order preserved):",unique_list)