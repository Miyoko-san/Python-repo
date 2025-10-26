l = [2, 5, 13, 10, 6, 55]

def div(n):
    if (n%5 == 0):
        return True
    return False

divisible = filter(div, l)
print(list(divisible))