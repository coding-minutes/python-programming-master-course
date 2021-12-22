## Exercise - 11
### Problem Statement
* **You're Given a string st.** **Arrange the string characters in such a way that lowercase letters should come first.**
  **The lowercase and Uppercase letter should be in the same order as in the input string.**
* **`Print the new string.`**



### Example -
```shell
Inputs : “HellO”

Output = ellHO

Inputs : "WoRLd"

Output : odWRL
```

### Solution 
```python
import sys
st = sys.argv[1]

# Write your logic here
left=''
right=''
for i in st:
    if i in "abcdefghijklmnopqrstuvwxyz":
        left+=i
    else:
        right+=i
print(left+right)
```
**Note**
* you can also directly output there is no need to make new string.