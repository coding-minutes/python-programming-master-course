<center><h2>Exercise - 16</h2> </center>

### Problem Statement :-
* **Given a list of tuples, where each tuple is (string and its magnitude),
  you have to write a python program to join all the strings with maximum magnitudes.**

### Example :-
```shell

Input :  [(“Hello Buddy”, 11), (“sample”, 6), (“to”, 2), (“how are you”, 11)]

Output: “Hello Buddy how are you”

Explanation: 11 is the maximum tuple element and concatenation of keys yield this result.


```



### Solution :-
```python
import sys
strings = [ele for ele in sys.argv[1].split(',')]
magnitudes = [int(ele) for ele in sys.argv[2].split()]

lst_of_tuples = [(strings[i], magnitudes[i]) for i in range(len(strings))]

# Write you code here
max_ele=-1000
for ele in lst_of_tuples:
    if(ele[1]>max_ele):
        max_ele=ele[1]
s=""
for ele in lst_of_tuples:
    if(ele[1]==max_ele):
        s+=ele[0]+" "
print(s.strip())
# end of code here.
```








