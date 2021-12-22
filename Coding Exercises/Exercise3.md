## Exercise - 3
### Problem statement 
* **_You are given 2 variables num1 & num2.
  You have to swap the values of these variables,
  such that the value of the variable num1  comes to variable num2 ,
  and value of num2 comes to num1 ._**

#### E.g.
```shell
num1 = 5

num2 = 10



After swapping,

num1 is 10, and num2 is 5



Note: There is no need to print the variables,
      You just have to swap num1 and num2
```
### Solution - 1
```python
import sys
num1, num2 = sys.argv[1], sys.argv[2]

# Write your code here
temp=num1
num1=num2
num2=temp

# Code ends here
```
### Solution - 2
```python
import sys
num1, num2 = sys.argv[1], sys.argv[2]

# Write your code here
num1,num2=num2,num1


# Code ends here

```
