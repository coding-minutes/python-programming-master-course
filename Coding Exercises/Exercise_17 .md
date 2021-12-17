<center><h2>Exercise - 17</h2> </center>

### Problem Statement :-
* **Given a list of tuples, each tuple has 2 integer numbers.** 
* **Your task is to write a python program that returns a list of tuples where
you have to convert the first element to positive magnitude while the second
element to the negative magnitude of each tuple.**

### Example :-
```shell

Input :
lst_of_tup = [(3, -1), (-4, -3), (1, 3), (-2, 5), (-4, 2), (-9, -3)]

Output :

[(3, -1), (4, -3), (1, -3), (2, -5), (4, -2), (9, -3)]


```
**`Explanation:`** All the first elements are positive, and 2nd elements are negative, as desired.


### Solution :-
```python
import sys
first = [int(i) for i in sys.argv[1].split()]
second = [int(i) for i in sys.argv[2].split()]

lst_of_tup = []
for i in range(len(first)):
    lst_of_tup.append((first[i], second[i]))
    
# Write your code here
new_lst=[]
for ele in lst_of_tup:
    temp=(abs(ele[0]),-abs(ele[1]))
    new_lst.append(temp)
print(new_lst)
# Code ends here
```








