arr = [-4, 3, -9, 0, 4, 1]
p=0
n=0
z=0
size = len(arr)

for v in arr:
    if v > 0:
        p += 1
        continue
    if v < 0:
        n += 1
        continue
    z += 1
print('{:.6f}'.format(p/size))
print('{:.6f}'.format(n/size))
print('{:.6f}'.format(z/size))

