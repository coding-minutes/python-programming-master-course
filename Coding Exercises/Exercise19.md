<center><h2>Exercise - 19</h2> </center>

### Problem Statement :-
* **You're given with a list of N elements.
  Your task is to print the maximum occurrence Element from the list**

```shell

Inputs: list of N elements

Outputs: Maximum frequency Element

```

### Example :-
```shell
Input: [a , b , a , c , a , b , d , c , a]

Output: a
```


### Solution :-
```python
import sys
lst = [i for i in sys.argv[1].split()]

# Write your code here
s=set(lst)
maxi=-1000
res=""
for i in s:
    if(lst.count(i)>maxi):
        maxi=lst.count(i)
        res=i
print(res)
# Code ends here
```

**Note:**
* `hey you can also use dictionary data structure but you can also try this method.`


















