import re
import sys
import time
def cocktailSort(a):
    n = len(a)
    swapped = True
    start = 0
    end = n - 1
    temp = 0
    while (swapped == True):

        # restablecer Flag de swap al entrar en el bucle,
        # porque podría ser cierto desde una iteración anterior.
        swapped = False

        # bucle de izquierda a derecha igual que la ordenación de burbujas
        for i in range(start, end):
            if (a[i] > a[i + 1]):
                temp = a[i]
                a[i] = a[i + 1]
                a[i + 1] = temp
                swapped = True

        # si no se mueve nada, entonces el array se ordena.
        if (swapped == False):
            break

        # de lo contrario, restablece la bandera intercambiada para
        # que pueda ser utilizada en la siguiente etapa
        swapped = False

        # retroceder el punto final en uno, porque el elemento del
        # final está en su lugar correcto
        end = end - 1

        # de derecha a izquierda, haciendo la misma comparación que
        # en la etapa anterior
        for i in range(end - 1, start - 1, -1):
            if (a[i] > a[i + 1]):
                temp = a[i]
                a[i] = a[i + 1]
                a[i + 1] = temp
                swapped = True

        # aumentar el punto de partida, ya que la última etapa habría
        # desplazado el siguiente número más pequeño al lugar que le corresponde.
        start = start + 1


# Driver code
with open('D:\WorkSpaces\Python/5th Semester\FLP\CocktailSort-Python\data/100.txt') as f:
    contents = f.readlines()
    stripped = [s.strip() for s in contents]
    Array100 = [int(x) for x in stripped]
with open('D:\WorkSpaces\Python/5th Semester\FLP\CocktailSort-Python\data/1000.txt') as f1:
    contents = f1.readlines()
    stripped = [s.strip() for s in contents]
    Array1000 = [int(x2) for x2 in stripped]
with open('D:\WorkSpaces\Python/5th Semester\FLP\CocktailSort-Python\data/2000.txt') as f2:
    contents = f2.readlines()
    stripped = [s.strip() for s in contents]
    Array2000 = [int(x3) for x3 in stripped]
with open('D:\WorkSpaces\Python/5th Semester\FLP\CocktailSort-Python\data/3000.txt') as f3:
    contents = f3.readlines()
    stripped = [s.strip() for s in contents]
    Array3000 = [int(x4) for x4 in stripped]
with open('D:\WorkSpaces\Python/5th Semester\FLP\CocktailSort-Python\data/4000.txt') as f4:
    contents = f4.readlines()
    stripped = [s.strip() for s in contents]
    Array4000 = [int(x5) for x5 in stripped]
with open('D:\WorkSpaces\Python/5th Semester\FLP\CocktailSort-Python\data/5000.txt') as f5:
    contents = f5.readlines()
    stripped = [s.strip() for s in contents]
    Array5000 = [int(x6) for x6 in stripped]
with open('D:\WorkSpaces\Python/5th Semester\FLP\CocktailSort-Python\data/6000.txt') as f6:
    contents = f6.readlines()
    stripped = [s.strip() for s in contents]
    Array6000 = [int(x7) for x7 in stripped]
with open('D:\WorkSpaces\Python/5th Semester\FLP\CocktailSort-Python\data/7000.txt') as f7:
    contents = f7.readlines()
    stripped = [s.strip() for s in contents]
    Array7000 = [int(x8) for x8 in stripped]
with open('D:\WorkSpaces\Python/5th Semester\FLP\CocktailSort-Python\data/8000.txt') as f8:
    contents = f8.readlines()
    stripped = [s.strip() for s in contents]
    Array8000 = [int(x9) for x9 in stripped]
with open('D:\WorkSpaces\Python/5th Semester\FLP\CocktailSort-Python\data/9000.txt') as f9:
    contents = f9.readlines()
    stripped = [s.strip() for s in contents]
    Array9000 = [int(x10) for x10 in stripped]
with open('D:\WorkSpaces\Python/5th Semester\FLP\CocktailSort-Python\data/10000.txt') as f10:
    contents = f10.readlines()
    stripped = [s.strip() for s in contents]
    Array10000 = [int(x11) for x11 in stripped]
with open('D:\WorkSpaces\Python/5th Semester\FLP\CocktailSort-Python\data/20000.txt') as f11:
    contents = f11.readlines()
    stripped = [s.strip() for s in contents]
    Array20000 = [int(x12) for x12 in stripped]
with open('D:\WorkSpaces\Python/5th Semester\FLP\CocktailSort-Python\data/30000.txt') as f12:
    contents = f12.readlines()
    stripped = [s.strip() for s in contents]
    Array30000 = [int(x13) for x13 in stripped]
with open('D:\WorkSpaces\Python/5th Semester\FLP\CocktailSort-Python\data/40000.txt') as f13:
    contents = f13.readlines()
    stripped = [s.strip() for s in contents]
    Array40000 = [int(x14) for x14 in stripped]
with open('D:\WorkSpaces\Python/5th Semester\FLP\CocktailSort-Python\data/50000.txt') as f14:
    contents = f14.readlines()
    stripped = [s.strip() for s in contents]
    Array50000 = [int(x15) for x15 in stripped]
#%%
t1 = time.time()
cocktailSort(Array100)
print("--- %s seconds ---" % (time.time() - t1))
t2 = time.time()
cocktailSort(Array1000)
print("--- %s seconds ---" % (time.time() - t2))
t3 = time.time()
cocktailSort(Array2000)
print("--- %s seconds ---" % (time.time() - t3))
t4 = time.time()
cocktailSort(Array3000)
print("--- %s seconds ---" % (time.time() - t4))
t5 = time.time()
cocktailSort(Array4000)
print("--- %s seconds ---" % (time.time() - t5))
t6 = time.time()
cocktailSort(Array5000)
print("--- %s seconds ---" % (time.time() - t6))
t7 = time.time()
cocktailSort(Array6000)
print("--- %s seconds ---" % (time.time() - t7))
t8 = time.time()
cocktailSort(Array7000)
print("--- %s seconds ---" % (time.time() - t8))
t9 = time.time()
cocktailSort(Array8000)
print("--- %s seconds ---" % (time.time() - t9))
t10 = time.time()
cocktailSort(Array9000)
print("--- %s seconds ---" % (time.time() - t10))
t11 = time.time()
cocktailSort(Array10000)
print("--- %s seconds ---" % (time.time() - t11))
t12 = time.time()
cocktailSort(Array20000)
print("--- %s seconds ---" % (time.time() - t12))
t13 = time.time()
cocktailSort(Array30000)
print("--- %s seconds ---" % (time.time() - t13))
t14 = time.time()
#%%
cocktailSort(Array40000)
print("--- %s seconds ---" % (time.time() - t14))
t15 = time.time()
#%%
cocktailSort(Array50000)
print("--- %s seconds ---" % (time.time() - t15))
#%%