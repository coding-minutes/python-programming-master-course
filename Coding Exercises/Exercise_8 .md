## Exercise - 8
### Problem statement
* **_You're given a number n._** **_You have to print the factorial of n._**

* **`Factorial of N = N * N-1 * N-2 * . . .  * 1`**

### Example - 
```shell
Input: N = 5

Output : 120

Explanation

5*4*3*2*1= 120
```
### Solution - 1
```python
import sys
N = int(sys.argv[1])

# Write you code here

fact=1
for i in range(1,N+1):
    fact*=i
print(fact)

# Code ends here
```
### Solution - 2 
**Using Recursion**
```python
import sys

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return fact(n-1)*n
        
N = int(sys.argv[1])

# Write you code here
print(fact(N))
# Code ends here
```