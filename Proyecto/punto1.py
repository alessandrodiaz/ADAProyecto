# PUNTO 1

class DisjointSetUnion:

    # Constructor para crear e inicializar sets de n items
    def __init__(self, n):

        self.rank = [1] * n
        self.parent = [i for i in range(n)]

    # Encuentra el set de un x dado

    def find(self, x):

        # Encuentra el representante del set al que x pertenece
        if (self.parent[x] != x):

            # Si x no es el padre de él mismo, entonces x no es el representante de su set
            self.parent[x] = self.find(self.parent[x])

            # Entonces recursivamente llamamos a Find con su padre y movemos el nodo de i directamente debajo del representante de este conjunto
        return self.parent[x]

    # Unir dos sets
    def union(self, x, y):

        # Buscar los sets actuales de x y
        xset = self.find(x)
        yset = self.find(y)

        # Si estan en el mismo set
        if xset == yset:
            return

        # Poner el elemento con menor rank debajo del de mayor rank, si los ranks son diferentes
        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset
        else:  # Si los ranks son iguales, mover y debajo de x, e incrementar el rank del árbol de x
            self.parent[yset] = xset
            self.rank[xset] = self.rank[xset] + 1

    # Leer instrucciones del archivo .in
    def leer_instrucciones(self, string):

        string = string.split(" ")

        query = str(string[0].rstrip())
        a = int(string[1].rstrip())
        b = int(string[2].rstrip())

        if query == "3":
            # Retorna True si ambos elementos pertenecen al mismo set
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


# Leer archivo
nombre_archivo = 'P1test2'

entrada = open(file='{}.in'.format(nombre_archivo), mode="r", encoding='utf-8')

primera_linea = entrada.readline()
primera_linea = primera_linea.split(" ")

num_departamentos = int(primera_linea[0])+1
num_queries = primera_linea[1]

mi_set = DisjointSetUnion(num_departamentos)

salida = open(file='{}.out'.format(nombre_archivo), mode="a", encoding='utf-8')
salida = open(file='{}.out'.format(nombre_archivo), mode="w", encoding='utf-8')


for x in entrada:
    mi_set.leer_instrucciones(str(x).replace("\t", " "))

entrada.close()
salida.close()
