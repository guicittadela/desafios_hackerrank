#
# Nesse desafio, temos duas posições iniciais (x1 e x2), e dois valores de intervalos (v1 e v2). Devemos prever se x1 e x2 serão iguais em algum
# momento, sabendo que x1 será somado a v1 e x2 será somado a v2. 
# Observação: no site existe uma informação de que o valores usados não serão maiores que 10000.
# 
#------ https://www.hackerrank.com/challenges/kangaroo/problem ------
#



x1 = 5000
v1 = 1
x2 = 4587
v2 = 2

for i in range(10000):      # contador de 0 a 10000
    if x1 == x2:            # quando x1 e x2 forem iguais, termina o laço e mostramos a mensagem 'YES'
        print('Yes')
        break
    else:
        x1 += v1            # se não forem iguais , somamos v1 e v2 a x1 e x2 respectivamente
        x2 += v2
if x1 != x2:
    print('NO')             # se o laço terminar e x1 não for igual a x2, mostramos a mensagem 'NO'.
    
