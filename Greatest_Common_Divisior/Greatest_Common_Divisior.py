# numpy and scipy are available for use
import numpy
import scipy

a = get_number()
b = get_number()

if b>a:
    n = b
    b = a
    a = n

if a%b == 0:
    res = b
else:
    m = 1
    while m<=b:
        if a%m==0 and b%m ==0:
            res = m
        m = m + 1

print(res)
