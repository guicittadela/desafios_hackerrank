#
#----- Desafio da escada tem o objetivo de criar uma escada do tipo:
#          .....#
#          ....##
#          ...###
#          ..####
#          .#####
#          ######


n = 6         # tamanho da escada
spc = '.'
tag = '#'
for x in range(n):                           # criei o laço para concatenar as strings spc e tag, onde em cada volta do laço é adicionada a quantidade correta de cada string
    print((spc * (n-1)+(tag * (x+1))))       # com ajuda do contador n e do valor de x que começa sendo o inverso de n na primeira volta, até chegar ao valor de n.
    n -=1                                    # a string spc será relacionada com o contador n enquanto a string tag será relacionada a x.
                                             # Então, na primeira volta será mostrado na tela a quantida de n-1 de spc e a quantidade de x+1 de tag, e em cada volta
                                             # vai decresendo em 1 o valor de n (logo também a quantidade de 'spc') e acrescido em 1 o valor de x (quantidade de tag).
    