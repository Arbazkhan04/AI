def depth(str):
    if not isinstance(str, (list, tuple)):
        return 0
    maxSoFar = 0
    for x in str:
        maxSoFar = max(maxSoFar, depth(x))
    return 1 + maxSoFar

print(depth('x'))
print(depth(('+', ('expt', 'x', 2), ('expt', 'y', 2))))