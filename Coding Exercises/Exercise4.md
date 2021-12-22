## Exercise - 4
### Problem statement 
* **_You are given with 2 integer numbers `num1` and `num2`_**
* **_Print the result of :_**
  * **_addition,  multiplication, division of `num1` and `num2`_**
  * **_is `num1` greater than `num2`_**
  * **_bitwise `AND` between `num1` and `num2`_**

```shell
e.g. -

Inputs :

num1 = 5, num2 = 4

Output :

9

20

1.25

True

4
```
### Solution
```python
import sys
num1, num2 = int(sys.argv[1]), int(sys.argv[2])

# Write your code here.

print(num1+num2)
print(num1*num2)
print(num1/num2)
print(num1>num2)
print(num1&num2)

# Code ends here.
```
