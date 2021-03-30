string = ''
n = 6
spc = '.'
tag = '#'
for x in range(n):
    print((spc * (n-1)+(tag * (x+1))))
    n -=1
    