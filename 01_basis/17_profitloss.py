cp = float(input("Enter the cost price: "))
sp = float(input("Enter the selling price: "))
if sp > cp:
    profit = sp - cp
    print("Profit:", profit)
    print("Profit percentage:", (profit / cp) * 100)
elif sp < cp:
    loss = cp - sp
    print("Loss:", loss)
    print("Loss percentage:", (loss / cp) * 100)
else:
    print("No profit, no loss.")    
