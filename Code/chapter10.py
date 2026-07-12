# Raising Exception.


def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception("Symbol must be a single character string.")
    if width <= 2:
        raise Exception("Width must be a greater than 2.")
    if height <= 2:
        raise Exception("Hieght must be a greater than 2.")

    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (" " * (width - 2)) + symbol)
        print(symbol * width)


for sym, w, h in (("*", 4, 4), ("O", 20, 5), ("x", 1, 3), ("ZZ", 3, 3)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print("An exception happened:" + str(err))

# Getting the Traceback as a string.
import traceback

try:
    raise Exception("This is the error message.")
except:
    errorFile = open("errorInfo.txt", "w")
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print("The Traceback info was written to errorInfo.txt.")

# Assertions
market_2nd = {"ns": "green", "ew": "red"}
mission_16th = {"ns": "red", "ew": "green", "nn": "yellow"}


def switchlights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == "green":
            stoplight[key] = "yellow"
        elif stoplight[key] == "yellow":
            stoplight[key] = "red"
        elif stoplight[key] == "red":
            stoplight[key] = "green"

    assert "red" in stoplight.values(), "Neither light is red!" + str(stoplight)


switchlights(mission_16th)

# Logging

import logging

logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s- %(message)s"
)
logging.debug("start of program")


def factorial(n):
    logging.debug("start of factorial(%s)" % (n))
    total = 1
    for i in range(1, n + 1):  # add 1
        total *= i
        logging.debug("i is:" + str(i) + "total is:" + str(total))
    logging.debug("end of factorial(%s)" % (n))
    return total


print(factorial(10))
logging.debug("end of program")

# Breakpoint
import random

heads = 0
for i in range(1, 1001):
    if random.randint(0, 1) == 1:
        heads = heads + 1
        if heads == 500:
            print("Halway done!")

print("heads came up", str(heads), "times.")
