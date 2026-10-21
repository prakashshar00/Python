n = int(input("Enter how many nymbers you want to input"))
numbers = []
for i in range(n):
  num = int(input(f"Enter number {i+1}:"))
  numbers.append(num)
print("\n The list of numbers entered is: ",numbers)

