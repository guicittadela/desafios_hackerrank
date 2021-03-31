#
# Uma universidade atribui notas de 0 a 100 a seus alunos, e se a nota for maior que 37 ele é arredondado sempre ao proximo múltiplo de 5,
# caso a diferença entre a nota e o próximo múltiplo de 5 for menor que 3. Se o número for menor ou igual a 37 não acontece nada a ele.
# ---- https://www.hackerrank.com/challenges/grading/problem ----
#


grades = [73, 67, 38, 33]

for v in range(len(grades)):
    if (grades[v] > 37) and ((grades[v] % 5) != 0):        # quando o valor de v n for múltiplo de 5, 
                                                           #e se o resto da divisão por 5 for menor que 3 
        if (5 - (grades[v]%5)<3):                          # faz se a conta da linha 13, onde será somado o resto da divisão ao valor de v
            grades[v] = grades[v] + 5 -(grades[v] % 5)

        
    
            
            
    

