lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

for v in lista:
    if (v % 3 == 0 and v % 5 == 0 ):
        print("FizzBuzz")
        continue
    
    if (v % 3 == 0):
        print('Fizz')
        continue
    
        
    if (v % 5 == 0):
        print('Buzz')
        continue
    
    print(v)