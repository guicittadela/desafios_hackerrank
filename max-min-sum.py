#
#----- Dados 5 números inteiros positivos, encontrar a soma máxima e a soma mínima
#----- usando exatamente 4 números do array
#----- https://www.hackerrank.com/challenges/mini-max-sum/problem
#


arr = [7, 3, 5, 1, 9]     #array com 5 números inteiros
soma_min = 0              #váriavel que será usada para a soma mínima
soma_max = 0              #váriavel que será usada para a soma mínima
arr.sort()                #ordena o array em ordem crescente

for v in arr[:4]:         # como a lista está ordenada, fica fácil achar a soma mínima, pois os 4 primeiros números, serão os 4 menores do array
    soma_min+=v           # esse laço for, percorre os 4 primeiros números do array, e faz a soma mínima

for v in arr[-4:]:        # esse laço for, percorre os 4 últimos números do array, e faz a soma máxima
    soma_max+=v

print(f'A soma máxima é: {soma_max} e a soma mínima: {soma_min}')



    

    
    
