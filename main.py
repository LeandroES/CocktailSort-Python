def cocktailSort(a, n):
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
    for i in range(len(a)):
        print("%d" % a[i])


# Driver code
a = [1522425, 10, 5, 6, 165, 1, 84, 56, 1523]
n = len(a)
cocktailSort(a, n)