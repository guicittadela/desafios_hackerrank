arr = [
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
]
d1 = 0
d2 = 0
cont_coluna = 0
idx_coluna = len(arr) - 1

for idx, value in enumerate(arr):
    d1 = value[cont_coluna] + d1
    cont_coluna += 1
    d2 = value[idx_coluna] + d2
    idx_coluna -= 1

print(abs(d1 + d2))

    


    
    