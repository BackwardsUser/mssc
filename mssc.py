#!/usr/bin/env python
# Minecraft Block Num to Stack Size
import argparse
import math

totalStackSize = 64

def stackSize(num):
    return num / totalStackSize

def getDecimal(raw):
    stacksWhole = math.floor(raw)
    return raw - stacksWhole

def getFinalStackSize(decimal):
    return decimal * totalStackSize

parser = argparse.ArgumentParser(description="Block Quantity to Stack Numbers")
parser.add_argument('num', help="Number of Items needed for project.")

num = int(parser.parse_args().num, base=10)
stacksRaw = stackSize(num)

stacks = math.floor(stacksRaw)
items = math.floor(getFinalStackSize(getDecimal(stacksRaw)))
stackPlural = "s" if stacks > 1 else ""
itemPlural = "s" if items > 1 else ""

print(f"The stacks needed for {num} items is, {stacks} stack{stackPlural}, {items} item{itemPlural}.")
