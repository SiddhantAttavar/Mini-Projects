from time import time
from sys import stdout

l = int(input()) #I gave 0 as input
r = int(input()) #I gave 10^9 as input

res1 = res2 = []

st1 = time()
for i in range(l, r + 1):
    if (i % 3) == 0:
        res1.append(i)
et1 = time()

st2 = time()
l = l if l % 3 == 0 else l + (3 - l % 3)
for i in range(l, r + 1, 3):
    res2.append(i)
et2 = time()

t1 = (et1 - st1) / 1000
t2 = (et2 - st2) / 1000

print('Are the results same: ' + ('Yes' if res1 == res2 else 'NO'))
print('Time taken for 1st algorithm: ' + str(t1) + 'seconds')
print('Time taken for 2nd algorithm: ' + str(t2) + 'seconds')
print('The faster algorithm is: ' + ('1st' if t1 < t2 else '2nd'))
print('It is ' + str(max(t2 / t1, t1 / t2)) + 'times faster')
