def sravnenie(a,b,c,d):
    if (a>=0 | b>=0 | c>=0 | d>=0):
        if ((c-a)>=1 and (d-b)>=1) :print('Да') 
        else:
            if ((c-d)>=1 and (d-a)>=1) :print('Да') 
            else: print('Нет')
    else: print('Числа должны быть целыми и неотрицательными') 
print('Введите длину первого прямоугольника') 
try:
    a = int(input()) 
except ValueError:
    print('Число должно быть целым и неотрицательным')
    exit() 
try:
    print('Введите ширину первого прямоугольника') 
    b = int(input()) 
except ValueError: 
    print('Число должно быть целым и неотрицательным') 
    exit()  
try:
    print('Введите длину второго прямоугольника')
    c = int(input()) 
except ValueError:
    print('Число должно быть целым и неотрицательным') 
    exit()  
try:
    print('Введите длинну второго прямоугольника')
    d = int(input()) 
except ValueError:
    print('Число должно быть целым и неотрицательным') 
    exit() 
sravnenie(a,b,c,d)
