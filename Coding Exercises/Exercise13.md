<center><h2>Exercise - 13</h2> </center>

### Problem Statement :-
* **`Given a 2D array calculate the sum of its principal diagonal elements.`**



### Example :-
```shell

Inputs:  [ [3,7], [0,-2] ]

Output : 1

Explanation : 3 - 2 = 1



Input: [ [1,3,5], [1,4,6], [7,6,9] ]

Output: 14
```

**Explanation** : `1 +  4 + 9 = 14`

### Solution :-
```python
def diagonal_sum(array):
    # Write your logic here.
    # you should always have 1 level of indentation
    result = 0
    for i in range(0,len(array)):
        result+=array[i][i]
        
    print(result)
```
**Explanation :-** 
> As we know in principal diagonal i is equal to j . 
>  So that is why here we use result += array[i][i]