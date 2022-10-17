import numpy
import scipy

a = get_number()
res = 0;

while a !=1:
    if a%2!=0:
        a = a + 1
    else:
        a = a/2
    res = res + 1

print(res)
