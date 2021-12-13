## Exercise - 5
### Problem statement 
* **_In this question, you have to check whether the input year is a leap year or not?_**

**_E.g._**

```shell
Input - 2017

Output - Not a leap year



Input - 2012
Output - Leap year

```
### Leap Year ?
* **_`A year which can be divided by 4 (but not by 100)  or 400 is known as leap year.`_** 
### Solution
```python
import sys
year = int(sys.argv[1])

# Write your code here

if( year % 400 == 0):
    print("Leap year")
elif( year % 4 == 0 and year % 100 !=0):
    print("Leap year")
else:
    print("Not a leap year")

# Code end
```



