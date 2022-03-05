import sys
N = int(sys.argv[1])

# Write your code here

sum = 0
while (N>0):
    remainder = N%10
    sum += remainder
    N//=10
    
print (sum)

# Code ends here