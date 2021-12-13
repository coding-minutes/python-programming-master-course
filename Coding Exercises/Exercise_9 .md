## Exercise - 9
### Problem statement
* **_You are given with an integer number N._** **_You have to print the sum of each digit of N._**

### Example -
```shell
Input: N = 2534

Output: 14

Explanation : 2+5+3+4 = 14
```
### Solution - 1
```python
import sys
N = int(sys.argv[1])

# Write your code here
dig_sum=0

while(N!=0):
    rem=N%10
    dig_sum+=rem
    N//=10
    
print(dig_sum)

# Code ends here
```
### Solution - 2
**Using Recursion**
```python
import sys
def digit_sum(n):
    if(n==0):
        return 0 
    else:
        return n%10 + digit_sum(n//10)
    
N = int(sys.argv[1])

# Write your code here
print(digit_sum(N))

# Code ends here
```