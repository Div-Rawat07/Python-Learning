#  Print count down using for loop and using time module having 1 sec gap

import time

count = int(input("Enter the counter number: "))

print("\n Countdown start now..!! ")
for i in range(count,0 , -1):
    print(i)
    time.sleep(1)

print("WOHOOOO Happpyyy NewYearrr..!!")