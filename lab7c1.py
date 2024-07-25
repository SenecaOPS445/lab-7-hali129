#!/usr/bin/env python3
# Student ID: hali129
from lab7c import *
t1 = Time(8, 0, 0)
t2 = Time(8, 55, 0)
t3 = Time(9, 50, 0)

td = Time(0, 50, 0)

tsum1 = sum_times(t1, td)
tsum2 = sum_times(t2, td)
tsum3 = sum_times(t3, td)

ft = format_time
print(ft(t1), '+', ft(td), '-->', ft(tsum1))
print(ft(t2), '+', ft(td), '-->', ft(tsum2))
print(ft(t3), '+', ft(td), '-->', ft(tsum3))

# Testing change_time
t4 = Time(9, 50, 0)
change_time(t4, 1800)
print(ft(t4))  # '10:20:00'
change_time(t4, -1800)
print(ft(t4))  # '09:50:00'
