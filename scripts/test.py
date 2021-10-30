import operator

action = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "**": pow
}

print(action["*"](4,15))