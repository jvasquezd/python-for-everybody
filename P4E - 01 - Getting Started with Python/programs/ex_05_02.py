largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        fval = int(num)
        if smallest is None or fval < smallest:
            smallest = fval
            print("Smallest: ", smallest, fval)
        elif largest is None or fval > largest:
            largest = fval
            print("Largest: ",largest, fval)
    except:
        print("Invalid input")
        continue
    
    
print("Maximum is", largest)
print("Minimun is", smallest)