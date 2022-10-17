# numpy and scipy are available for use
import numpy
import scipy

a = get_number()

b = list()
for i in range(a):
    b.append(get_number())

#print(a)
#print(b)

c = list()
x = b[1] + b[a-1]
#print(x)
c.append(x)
for i in range(1,a-1):
    x = b[i-1]+ b[i+1]
    c.append(x)

x = b[0] + b[a-2]

c.append(x)
print(a)
print(*c)
