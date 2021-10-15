# import sys
# distance, time = int(sys.argv[1]), int(sys.argv[2])

# Write you code here

distance=21
time=40

basePrice = 50
freeKms = 5
perKms = 10
freeMins = 15
perMins = 2

if (distance <= 5):
    distance_amount = 0
else:
    distance_amount = (distance-freeKms)*perKms
    
    
if (time <= 15):
    time_amount = 0
else:
    time_amount = (time-freeMins)*perMins
    

Total_Amount = basePrice + distance_amount + time_amount

print(Total_Amount)

# Code ends here