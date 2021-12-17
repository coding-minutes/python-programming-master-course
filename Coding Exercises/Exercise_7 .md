## Exercise - 7
### Problem statement
* **_You are given the distance(in km) and time(in mins)._** 
* **_Calculate the Cab fare for the passenger, using the following properties :_**

------------------------------------------------------------

* **`basePrice`** : 50Rs  (this price will be charged in all the cases)

* **`freeKms`** : 5Rs  (If you travel for 5km or less, you won't be charged extra for distance.. )

* **`perKm`**: 10Rs (If you travel more than 5km, then you will be charged 10rs per km on the additional distance apart from the first 5kms.)

* **`freeMins`** : 15Rs (If you are in the cab for less or equal to 15 minutes, you won't be charged extra for the time. )

* **`perMins`** : 2Rs (If you are in the cab for more than 15 min, then 2rs per min will be charged on the additional time apart from first 15kms)

------------------------------------------------------------



### Example -

```shell
distance = 21km and time taken = 40mins


Base Price = Rs.50

Amount for distance = (21-5)*10 => 16*10 => Rs. 160.           

[because for the first 5 km you won't be charged extra]   


Amount for time = (40-15)*2 => 25*2 => Rs. 50.                 

[because for the first 15 mins you won't be charged ]   


Total Amount = Base Price + amount for distance + amount for time

Total Amount = 50 + 160 + 50

Total Amount = Rs. 260


Output: 260
```
### Solution 
```python
import sys
distance, time = int(sys.argv[1]), int(sys.argv[2])

# Write you code here
basePrice=50

amountForDistance=0
if(distance<=5):
    amountForDistance=5
else:
    amountForDistance=(distance-5)*10
    
amountFortime=0
if(time<=15):
    amountFortime=15
else:
    amountFortime=(time-15)*2

total= basePrice +amountForDistance+amountFortime
print(total)

# Code ends here

```
