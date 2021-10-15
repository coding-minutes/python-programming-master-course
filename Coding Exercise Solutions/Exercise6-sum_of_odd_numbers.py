import sys
N = int(sys.argv[1])

# Write your code here
sum = 0
for i in range(1,N+1):
    if (i%2 != 0):
        sum+=i;
    else:
        continue;
        
print(sum)

# Code ends here