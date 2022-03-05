import sys
year = int(sys.argv[1])

# Write your code here
if (year%4==0):
    if (year%100==0):
        if (year%400==0):
            print("Leap year")
        else:
            print("Not a leap year")
        
    else:
        print("Leap year")


   
# Code end