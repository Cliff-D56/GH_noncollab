def RFib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return RFib(n-1) + RFib(n-2)
