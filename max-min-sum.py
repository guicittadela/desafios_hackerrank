#
#----- Dados 5 números inteiros positivos, encontrar a soma máxima e a soma mínima
#----- usando exatamente 4 números do array
#----- https://www.hackerrank.com/challenges/mini-max-sum/problem
#


arr = [7, 3, 5, 1, 9]
soma_min = 0
soma_max = 0
arr.sort()   #ordena a 
print(arr)
for v in arr[:4]:
    soma_min+=v

for v in arr[-4:]:
    soma_max+=v

print(f'A soma máxima é: {soma_max} e a soma mínima: {soma_min}')



    

    
    
