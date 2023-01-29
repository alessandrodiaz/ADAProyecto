# PUNTO 1
from pathlib import Path


class DisjointSetUnion:

    def __init__(self, n):

        self.rank = [1] * n
        self.padre = [i for i in range(n)]

    # Encuentra el representante del set al que x pertenece
    def find(self, x):
        if (self.padre[x] != x):

            # Si x no es el padre de él mismo, entonces no es el representante de su set
            # Se hacen llamados recursivos
            self.padre[x] = self.find(self.padre[x])
        return self.padre[x]

    # Unir dos sets
    def union(self, x, y):

        # Buscar los sets actuales de x y
        xset = self.find(x)
        yset = self.find(y)

        # Si estan en el mismo set
        if xset == yset:
            return

        if self.rank[xset] < self.rank[yset]:
            self.padre[xset] = yset
        elif self.rank[xset] > self.rank[yset]:
            self.padre[yset] = xset
        else:
            self.padre[yset] = xset
            self.rank[xset] = self.rank[xset] + 1

    # Leer instrucciones del archivo .in
    def leer_instrucciones(self, string):

        string = string.split(" ")

        query = str(string[0].rstrip())
        a = int(string[1].rstrip())
        b = int(string[2].rstrip())

        if query == "3":
            # Retorna true si ambos elementos pertenecen al mismo set
            salida.write(str(mi_set.find(a) == mi_set.find(b)).lower()+"\n")
        elif query == "2":
            i = a
            # Unir departamentos entre A y B
            while i <= b:
                mi_set.union(a, i)
                i = i+1
        elif query == "1":
            # Unir departamentos A y B
            mi_set.union(a, b)


# Poner nombre del archivo de lectura, sin la extension
# Toma el archivo 1input.in y escribe en la salida .out
# Ingresar el numero del test

nombre_archivo = '1'

entrada = open(file=(Path(__file__).parent /
               '{}input.txt'.format(nombre_archivo)), mode="r", encoding='utf-8')

primera_linea = entrada.readline()
primera_linea = primera_linea.split(" ")

num_departamentos = int(primera_linea[0])+1

mi_set = DisjointSetUnion(num_departamentos)

salida = open(file=(Path(__file__).parent /
              '{}output.txt'.format(nombre_archivo)), mode="a", encoding='utf-8')
salida = open(file=(Path(__file__).parent /
              '{}output.txt'.format(nombre_archivo)), mode="w", encoding='utf-8')


for x in entrada:
    mi_set.leer_instrucciones(str(x).replace("\t", " "))

entrada.close()
salida.close()
