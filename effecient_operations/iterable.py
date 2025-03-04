
# Delete elements/Filter list
# ---------------------------
def is_even(num:int):
    return not num % 2
l = list(range(10))
l[:] = filter(is_even, l)
print(l)



