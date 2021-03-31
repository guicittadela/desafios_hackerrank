#
# Desafio das velas de aniversário:
#  
# https://www.hackerrank.com/challenges/birthday-cake-candles/problem
#
#

candles = [3, 2, 1, 3]
candles.sort()        # ordenei a lista de forma crescente
n = len(candles)      # váriavel 'n' é igual ao tamanho da lista 
x=0                   # contador 
for v in range(n):    # laço 'for' para contar a quantidade de velas com o valor mais alto
    
    if candles[v] == candles[-1]:         #compara os valores e quando forem iguais acrescenta +1 ao valor de 'x'
        x+=1
print(x)


"""
####--------------desafio postado no padrão do site:

def birthdayCakeCandles(x):
    candles.sort()
    n = len(candles)
    x=0
    for v in range(n):
        
        if candles[v] == candles[-1]:
            x+=1
    return x
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
"""