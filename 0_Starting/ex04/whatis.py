import sys

if len(sys.argv) < 2:
	exit()
elif len(sys.argv) > 2:
	raise AssertionError("more than one argument is provided")

num = sys.argv[1]

num = num.strip()

idx = 0
if num[idx] == '+' or num[idx] == '-':
	idx = 1

if num.find("__") != -1:
	raise AssertionError("argument is not an integer")
num = num.replace("_", "")

if num[idx:].isdecimal():
	num = int(num)
else:
	raise AssertionError("argument is not an integer")

if num % 2 == 0:
	print("I'm Even")
else:
	print("I'm Odd")