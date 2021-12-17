<center><h2>Exercise - 15</h2> </center>

### Problem Statement :-
* **Given a list (lst) of N Numbers, Print the second largest element if there exists any, otherwise print None**

```shell

Inputs: List of N elements

Output: Print the Second largest Element if there's any. Otherwise Print None

```
### Example :-
```shell
Input : [5,2,7,9,3,2,0]

Output : 7



Input : [8,8,8]

Output : None
```



### Solution -1 :-
```python
import sys
lst = [int(i) for i in sys.argv[1].split()]

# Write your code here
lst.sort(reverse=True)
highest=lst[0]
flag=True
for i in lst:
    # case where we get second largest 
    if(i!=highest):
        print(i)
        flag=False
        break
if flag==True:
    print(None)
# Code ends here
    
```

### Note
* for this question there can be various methods 
  * you can use quick select algorithm
  * you can sort then find highest then get maximum
    through those items where element is not equal to highest and print it.






