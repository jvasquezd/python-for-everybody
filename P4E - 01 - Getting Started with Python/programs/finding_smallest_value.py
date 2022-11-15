
smallest_so_far = 99999
print("Before", smallest_so_far)

for the_num in [9,41,12,3,74,15]:
    if the_num < smallest_so_far:
        smallest_so_far = the_num
    print(smallest_so_far, the_num)
print("After", smallest_so_far)


smallest = None #flag value
print('Before')
for value in [9,41,12,3,74,15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print("After", smallest)