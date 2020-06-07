import math
a = 10
b = -5
c = 4

delta = (b ** 2) - 4 * a * c 
if delta > 0 :
    x_ = (-b + math.sqrt(delta)) / (2 * a) 
    x__ = (-b - math.sqrt(delta)) / (2 * a)
    print(x_, x__)
if delta == 0 :
    x = -b / (2 * a)
    print (x)
if delta < 0 :
    print("Não existe.")

