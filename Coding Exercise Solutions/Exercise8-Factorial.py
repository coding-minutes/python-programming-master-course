import sys
N = int(sys.argv[1])

# Write you code here

factorial = 1

for i in range(1,N+1):
    factorial*=i
    
print(factorial)

# Code ends here