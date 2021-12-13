## Exercise - 11
### Problem Statement
* **You're Given 2 strings s1 and s2.** **You have to check if s1 is a subsequence of s2.**
* **Subsequence means -** `if all the characters of string s1 appear in the string s2. S2 can have more or equal numbers of characters.`




### Example -
```shell

Inputs :

s1 = "cdngmutes"

s2 = "coding minutes"

Output = True



Inputs :

s1 = "cdng python"

s2 = "coding minutes"

Output : False


```

### Solution 
```python
import sys
s1, s2  = sys.argv[1], sys.argv[2] 
# Write your logic here
flag=True
for i in s1:
    if s2.find(i)== -1:
        flag=False
        break
print(flag)
```
