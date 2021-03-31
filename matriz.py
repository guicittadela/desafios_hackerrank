# 
# 
#------ Dada uma matriz quadrada, de qualquer tamanho, 
#------ calcular a diferenca absoluta entre a soma das duas diagonais
#------ https://www.hackerrank.com/challenges/diagonal-difference/problem
#
arr = [
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4],
]
d1 = 0            #soma da primeira diagonal
d2 = 0            #soma da segunda diagonal
cont_coluna = 0
idx_coluna = len(arr) - 1

for idx, value in enumerate(arr):   # como o laço percorre uma matriz, precisamos acessar os indíces da matriz e também os valores dentro do array
    d1 = value[cont_coluna] + d1    # percebi durante a construção do código que as diagonais seguem um padrão de posicionamento na matriz:
    cont_coluna += 1                # a primeira diagonal (d1) vai acessar sempre os itens que possum as coordenadas (value e idx, onde value são as colunas e idx as linhas) iguais. 
                                    # Por exemplo em uma matriz 4x4 os valores de d1 estarão sempre posicionados em (0,0), (1,1), (2,2), (3,3). Assim criei o contador "cont_coluna"
                                    # começando em 0, e em cada loop é acrescido +1 até o final do laço "for". Após acessado o valor correto, o valor é adicionado e somado a d1.





    d2 = value[idx_coluna] + d2     # já para segunda diagonal o padrão é diferente, pois no primeiro laço o valor da coluna (value) precisa ser o último item (coordenada (0,3)),
    idx_coluna -= 1                 # assim criei o contador idx_coluna que vai ser igual ao tamanho da array -1 (no caso de uma matriz 4x4, idx coluna vai ser igual a 3)
                                    # no primeiro loop então o valor acessado será o de índice (0,3) e em cada loop do laço, o valor idx vai aumentando enquanto o de value 
                                    # vai diminuindo (linha 29). Aapós acessado o valor correto, o valor é adicionado e somado a d2.


print(abs(d1 + d2))                 # Ao final dos dois laços, é feita a soma absoluta das diagonais. 


    


    
    