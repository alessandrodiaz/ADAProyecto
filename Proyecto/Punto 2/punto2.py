# PUNTO 2
from pathlib import Path


class Nodo:

    def __init__(self, letra):
        self.letra = letra
        self.words = 0  # Palabras que desprenden de el
        self.sons = dict()
        self.end = False

    # Elije al nodo hijo que mas hijos tiene o, en caso de existir un empate
    # elige dado el orden lexicografico

    def elegir_siguiente(self):
        sons = self.sons
        l_s = list(sons)
        eleccion = sons[l_s[0]]

        for i in range(0, len(l_s)):
            if sons[l_s[i]].words > eleccion.words:
                eleccion = sons[l_s[i]]

            elif sons[l_s[i]].words == eleccion.words:
                if sons[l_s[i]].letra < eleccion.letra:
                    eleccion = sons[l_s[i]]

        return eleccion


class Trie:

    def __init__(self):
        self.root = Nodo("root")

    # Añade una nueva palabra al Trie
    # Complejidad O(n)

    def insertar(self, palabra):
        root = self.root

        for letra in palabra:
            if letra not in root.sons:
                root.sons[letra] = Nodo(letra)
            root.words = root.words + 1
            root = root.sons[letra]

        root.end = True

    # Busca si existe una palabra que contenga un prefijo dado
    # Complejidad O(n)

    def buscar_prefijo(self, palabra):
        root = self.root

        for letra in palabra:
            if letra not in root.sons:
                return False
            root = root.sons[letra]

        return True

    # Busca si el Trie contiene una palabra
    # Complejidad O(n)

    def buscar_palabra(self, palabra):
        root = self.root

        for letra in palabra:
            if letra not in root.sons:
                return False
            root = root.sons[letra]

        return root.end

    # Elimina una palabra de la estructura
    # Complejidad O(n)

    def eliminar_palabra(self, palabra):

        if self.buscar_palabra(palabra):
            root.words = root.words - 1

            for letra in palabra:
                root.sons[letra].words = root.sons[letra].words - 1

                if root.sons[letra].words == 0:
                    root.sons[letra] = null
                    break

                root = root.sons[letra]

        else:
            return "La palabra no pertenece a la estructura"

    # Busca la palabra que representa una mejor opcion para completar un texto dado

    def buscar_sugerencia(self, palabra):
        root = self.root
        sugerencia = ""

        for letra in palabra:
            if letra not in root.sons:
                break

            sugerencia = sugerencia + letra
            root = root.sons[letra]

        while root.end != True:
            root = root.elegir_siguiente()
            sugerencia = sugerencia + root.letra

        return sugerencia

    # Leer instrucciones del archivo .in

    def leer_instrucciones(self, string, out):

        string = string.split(" ")

        query = str(string[0].rstrip())
        s = str(string[1].rstrip())

        if query == "1":
            self.insertar(s)
        else:
            out.write(str(self.buscar_sugerencia(s)).lower() + "\n")
            print(self.buscar_sugerencia(s))


# Poner nombre del archivo de lectura, sin la extension
# Toma el archivo .in y escribe en la salida .out
PrefixTree = Trie()

nombre_archivo = '6'

entrada = open(file=(Path(__file__).parent /
               '{}input.txt'.format(nombre_archivo)), mode="r", encoding='utf-8')

primera_linea = entrada.readline()
primera_linea = primera_linea.split(" ")

salida = open(file=(Path(__file__).parent /
              '{}output.txt'.format(nombre_archivo)), mode="a", encoding='utf-8')
salida = open(file=(Path(__file__).parent /
              '{}output.txt'.format(nombre_archivo)), mode="w", encoding='utf-8')

for x in entrada:
    PrefixTree.leer_instrucciones(str(x).replace("\t", " "), salida)

entrada.close()
salida.close()
