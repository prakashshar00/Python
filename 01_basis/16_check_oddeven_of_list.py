n = int(input("Enter the number of elements in the list: "))
even_numbers = []
odd_numbers = []    
for i in range(n):
    num = int(input("Enter number: "))
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
print("Even numbers in the list:", even_numbers)
print("Odd numbers in the list:", odd_numbers)  