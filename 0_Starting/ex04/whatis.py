import sys

try:
    if len(sys.argv) < 2:
        exit()
    elif len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")

    num = sys.argv[1]
    try:
        num = int(num)
    except ValueError:
        raise AssertionError("argument is not an integer")

    if num % 2 == 0:
        print("I'm Even")
    else:
        print("I'm Odd")
except AssertionError as e:
    print("AssertionError:", e)
except Exception as e:
    print(f"{e.__class__.__name__}:", e)
