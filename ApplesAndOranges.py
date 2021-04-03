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
apples = [2, -2, 1]           # posições das maçãs
oranges = [1, 5, -6]          # posições das laranjas
m = 0                         # contador de maçãs
l = 0                         #contador de laranjas
for v in apples:              # laço que vai contar a quantidade de maçãs que caem no range (s:t)
    if t >= (v + a) >=s:      # soma o cada valor da lista 'apples' com valor de 'a' (posição da macieira), e caso seja um valor >=s e <= a t, é feito a soma 'm = m + 1' .
        m += 1      
for v in oranges:             # mesmo caso do laço acima, porém com os valores de 'b' e 'oranges'.
    if t >= (v + b) >=s:
        l += 1  

print(m)                      # ao final dos dois laços monstramos a quantidade de maçãs (m) e laranjas (l).
print(l)