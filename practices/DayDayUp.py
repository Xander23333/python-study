#DayDayUpQ1.py
dayup=1
daycontor=0.005
for i in range(1,366):
    if i%7 in [0,6]:
        dayup*=(1-0.01*daycontor)
    else:
        dayup*=(1+daycontor)
print(dayup)
