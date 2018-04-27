from time import *
start=process_time()
start2=perf_counter()
for i in range(1000000):
  i
end=process_time()
end2=perf_counter()
print("{:.4f} {:.4f}".format(end-start,end2-start2))

a=localtime()
print(strftime("%Y-%m-%d %b(%B) %a(%A) %H:%M:%S(%I:%M:%S %p)",a))
