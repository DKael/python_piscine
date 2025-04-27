import time

time_stamp = time.time()

print(f"Seconds since January 1, 1970: {time_stamp:,.4f} or {time_stamp:.2e} in scientific notation")
print(time.strftime("%b %d %Y"))