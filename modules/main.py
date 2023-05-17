# Do not modify these lines
__winc_id__ = "78029e0e504a49e5b16482a7a23af58c"
__human_name__ = "modules"

# Add your code after this line
import this

print(this)


def wait(seconds):
    import time

    time.sleep(seconds)


def my_sin(n):
    import math

    return math.sin(n)


def iso_now():
    from datetime import datetime

    time = datetime.now()
    time = time.strftime("%Y-%m-%dT%H:%M")

    return time


def platform():
    import sys

    return sys.platform


# Call functions
# wait(2)
# print(my_sin(2))
# print(iso_now())
# print(platform())
