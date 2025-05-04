from time import time
from time import strftime

time_stamp = time()

print(f"Seconds since January 1, 1970: {time_stamp:,.4f} or {time_stamp:.2e} in scientific notation")
print(strftime("%b %d %Y"))