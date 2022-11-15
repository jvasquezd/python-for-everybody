def computepay(h,r):
    if h < 40 :
        return h*r
    else :
        return (40*r + (h - 40)*r*1.5)

hrs = input("Enter Number of Hours worked:")
rt = input('Enter the required rate per hour: ')
hours = float(hrs)
rate = float(rt)

print("Pay",computepay(hours,rate) )