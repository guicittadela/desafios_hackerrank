#
# O objetivo desse desafio é contar a quantidade de maças e laranjas que caem na casa de 'Sam'. A casa de fica ao longo do eixo x
# e suas coordenadas são definidas por 's'(inicio) e 't'(fim). A macieira fica a esquerda da casa e sua posição é definida por 'a'.
# Já a laranjeira fica a direita da casa e sua posição é definida por 'b'. As frutas que caem são definidas de acordo com os valores do array
# correspondente. Os valores do array tem como referencial as posições 'a' e 'b'. Ou seja se o valor do array é 2, significa que a fruta caiu
# duas posições afastadas da árvore. Assim o algoritmo precisa somar a posição da árvore e a posição que o fruto caiu. Se o valor estiver
# na área da casa (entre 's' e 't'), logo ela caiu na casa, e deve ser contada ao final do código.
#
# ----- https://www.hackerrank.com/challenges/apple-and-orange/problem ----
#

s = 7
t = 11
a = 5
b = 15
apples = [2, -2, 1]
oranges = [1, 5, -6]
m = 0 
l = 0
for v in apples:
    if t >= (v + a) >=s:
        m += 1  
for v in oranges:
    if t >= (v + b) >=s:
        l += 1  

print(m)
print(l)