## Exercise - 2
### Problem statement 
* **_You are given a temperature in Celsius. 
  Your task is to convert the Celsius temperature to Fahrenheit._**
### Solution
```python
# Formula for converting celsius temp. to fahrenheit temp. is.....
# Let say temp. in Celsius scale is C and temp. in fahrenheit scale is F then ..
# F= 32 + ((9*C)/5)
import sys
C = float(sys.argv[1])
F = 32 + ((9*C)/5)
print(F)

```