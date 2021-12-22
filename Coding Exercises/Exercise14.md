<center><h2>Exercise - 14</h2> </center>

### Problem Statement :-
* **From a class of n students, you are given marks of students who appeared in a test.** 
  **Two or more students can have the same marks.**
  **Print the highest and second-highest marks in the class.**


### Example :-
```shell
Input : [78, 86, 66, 81, 66, 81, 50, 81, 23, 45, 79, 62, 86, 33]

Output :

86

81

```



### Solution -1 :-
```python
import sys
lst = [int(i) for i in sys.argv[1].split(',')]

# sort and find your result
# sorted in decreasing order 
lst.sort(reverse=True)
highest=lst[0]
print(highest)
for i in lst:
    # case where we get second largest 
    if(i!=highest):
        print(i)
        break
    
```

### Note
* for this question there can be various methods 
  * you can use quick select algorithm
  * you can sort then find highest then get maximum
    through those items where element is not equal to highest