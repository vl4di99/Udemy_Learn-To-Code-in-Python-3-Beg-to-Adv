import time as t

current_time = t.localtime()

print("It is " + str(current_time.tm_hour)+"h and "+ str(current_time.tm_min)+"min")

t.time() # epic time since 1st jan 1970

# Calculate delivery time with epic time

days_until_delivery = 16
delivery_time = t.time() + (86400*16)
print(t.localtime(delivery_time))