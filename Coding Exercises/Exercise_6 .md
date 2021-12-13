## Exercise - 6
### Problem statement 
* **_You are given with an integer Number N
  Your task is to find the sum of all odd numbers from 1 to N (Both inclusive)_**



### Example:
```shell
Input: N = 10

Output: 25
```
**Explanation: 1+3+5+7+9 = 25**

### Solution - 1
```python
import sys
N = int(sys.argv[1])

# Write your code here
Sum=0
for i in range(1,N+1,2):
    Sum+=i
print(Sum)
# Code ends here
```

### Solution - 2
```python
import sys
N = int(sys.argv[1])

# Write your code here
Sum=0
for i in range(1,N+1):
    if(i%2!=0):
      Sum+=i
print(Sum)
# Code ends here
```


