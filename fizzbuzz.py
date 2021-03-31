#
#
#----------INCOMPLETO--------
#
#



lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

for v in lista:
    if (v % 3 == 0 and v % 5 == 0 ):
        v = 'FizzBuzz'
        print(v)
        lista.append(v)
    elif (v % 3 == 0):
        
        v = ('Fizz')
        print(v)
        
    elif (v % 5 == 0):

        v = ('Buzz')
        print(v)
        
    
print(lista)