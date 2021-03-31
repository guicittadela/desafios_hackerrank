# 
# 
#----- Dada uma matriz de inteiros, calcule as proporções de seus elementos que são positivas, negativas e zero. 
#----- Imprima o valor decimal de cada fração em uma nova linha com 6 casas decimais após a vígula.
#----- https://www.hackerrank.com/challenges/plus-minus/problem
#

arr = [-4, 3, -9, 0, 4, 1]
p=0
n=0
z=0
size = len(arr)        

for v in arr:
    if v > 0:
        p += 1       #contador de números positvos
        continue
    if v < 0:
        n += 1       #contador de números negativos
        continue
    z += 1           #contador de zeros
print('{:.6f}'.format(p/size))     # print formatado com 6 números decimais após a vígula, cada print pega o valor de cada variavel e divide pelo tamanho da lista
print('{:.6f}'.format(n/size))
print('{:.6f}'.format(z/size))

