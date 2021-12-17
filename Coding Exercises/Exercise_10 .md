## Exercise - 10
### Problem Statement
* **You are given a string of odd length greater than equal to 7,
  print a new string made up of the middle three characters of the given 
  String.**

### Example -
```shell
Input : st

Output : middle string


Sample Cases:

Input : "JhonDipPeta"

Output :  Dip


Input  : "JaSonAy"

Output :  Son
```
### Solution 
```python
import sys
st = sys.argv[1]

# Write your logic Here
mid=len(st)//2
new_str=st[mid-1:mid+2]
print(new_str)
```