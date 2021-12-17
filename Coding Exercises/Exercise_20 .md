<center><h2>Exercise - 20</h2> </center>

### Problem Statement :-
* **Given a Dictionary `d` your task is to reverse the dictionary.
  Keys should be converted to Values and,
  Values should be converted to keys**

```shell
Inputs : Dictionary `d`

Outputs : Reverse of `d`
```
### Example :-
```shell
Input : { 1 : 'p' , 2 : 'q' , 3 : 'r' }

Output : { 'p' : 1 , 'q' : 2 , 'r' : 3 }
```


### Solution :-
```python
import sys
keys = [i for i in sys.argv[1].split()]
values = [int(i) for i in sys.argv[2].split()]

dic = dict()
for i in range(len(keys)):
    dic[keys[i]] = values[i]
    

# Write your code here

# Method -1
# rev_dic=dict()
# for key,value in dic.items():
#     rev_dic[value]=key

# Method -2
rev_dic={v:k  for k,v in dic.items()}
print(rev_dic)
# Code ends here
```








