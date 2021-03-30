arr = [4, 5, 5, 5, 6, 6, 4, 1, 4, 4, 3, 6, 6, 3, 6, 1, 4, 5, 5, 5]

arr.sort()
print(arr)
pares = 0
for  idx, v in enumerate(arr):
    arr.pop(idx)
    for idx2, v2 in enumerate(arr):
        if v == v2:
            pares+=1
            arr.pop(idx2)
    

print(pares)


    
        
        
