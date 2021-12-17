<center><h2>Exercise - 21</h2> </center>

### Problem Statement :-
* **Given a dictionary dic, count the pairs where the sum of keys and their respective values are equal.**

### Example :-
```shell
Input: {5:5, 8:9, 8:7, 1:2, 10:0, 7:8}

Output: 2

```
**Explanation:**
```shell
There are 2 pairs, where the sum of keys and their values are equal :

1. 5:5  and 10:0 , as 5+5 = 10+0 = 10

2. 8:7 and 7:8, as 8+7=7+8 = 15
```
### Solution :-
```python
import sys

keys = [int(k) for k in sys.argv[1].split()]

values = [int(v) for v in sys.argv[2].split()]



dic = {}

for k, v in zip(keys,values):

    dic[k] = v

   

# Write you code here

newdict = {}

for key,val in dic.items():

    if (key+val) in newdict:

        newdict[key+val] = newdict[key+val] + 1

    else:

        newdict[key+val] = 1

print(sum([1 for val in newdict.values() if val > 1]))
```


