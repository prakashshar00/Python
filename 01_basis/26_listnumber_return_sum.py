def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
n = int(input("Enter the number of elements in the list: "))
numbers = []    
for i in range (n):
    num = int(input(f"Enter element {i+1}: "))
    numbers.append(num)
result = sum_of_list(numbers)
print(f"The sum of the list is: {result}")