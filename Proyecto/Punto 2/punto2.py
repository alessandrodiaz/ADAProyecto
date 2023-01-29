class Nodo:

    def __init__ (self, letra):
        self.letra = letra
        self.words = 0 #Palabras que desprenden de el
        self.sons = dict()
        self.end = False


    #Elegir siguiente
    def elegir_siguiente(self):

        sons = self.sons
        l_s = list(sons)
        eleccion = sons[ l_s[0]]

        for i in range (0, len(l_s)):

            if sons[ l_s[i] ].words > eleccion.words:
                eleccion = sons[ l_s[i] ]
            elif sons[ l_s[i] ].words == eleccion.words:
                if sons[ l_s[i] ].letra < eleccion.letra:
                    eleccion = sons[ l_s[i] ]
                    
    
        return eleccion


class Trie:

    def __init__ (self):
        self.root = Nodo("root")
        

    # Insertar    
    def insertar (self, palabra):

        root = self.root
        
        for letra in palabra:
            #print(root.letra, root.words)
            
            if letra not in root.sons:
                root.sons[ letra ] = Nodo( letra )
            root.words = root.words + 1
            #print(root.letra, root.words)
            root = root.sons[ letra ]
            
        #print(root.letra, root.words)
        root.end = True


    #Buscar Prefijo
    def buscar_prefijo (self, palabra):

        root = self.root
        
        for letra in palabra:

            if letra not in root.sons:
                return False

            root = root.sons[ letra ]

        return True


    #Buscar Palabra
    def buscar_palabra (self, palabra):

        root = self.root

        for letra in palabra:

            if letra not in root.sons:
                return False

            root = root.sons[ letra ]

        return root.end


    #Eliminar Palabra
    def eliminar_palabra (self, palabra):

        root = self.root

        for letra in palabra:

            root.words = root.words - 1
            
            if root.sons[ letra ].words == 0:
                root.sons[ letra ] = null    
                break

            root.words = root.words + 1
            
            root = root.sons[ letra ]






    #buscarSugerencia
    def buscar_sugerencia(self, palabra):

        root = self.root
        sugerencia = ""

        for letra in palabra:
            #print(root.letra)
            if letra not in root.sons:
                break
            
            sugerencia = sugerencia + letra
            root = root.sons[letra]

        while root.end != True:
            
            root = root.elegir_siguiente()
            sugerencia = sugerencia + root.letra
            

        return sugerencia


    #Leer instrucciones
    def leer_instrucciones(self, string, out):

        string = string.split(" ")

        query = str(string[0].rstrip())
        a = str(string[1].rstrip())

        if query == "1":
            self.insertar(a)
        else:
            out.write(str (self.buscar_sugerencia(a)).lower() + "\n")
            print (self.buscar_sugerencia(a))


#Leer archivo
PrefixTree = Trie()

nombre_archivo = 'P2test2'

entrada = open(file='{}.in'.format(nombre_archivo), mode="r", encoding = 'utf-8')

primera_linea = entrada.readline()
primera_linea = primera_linea.split(" ")

salida = open(file='{}.out'.format(nombre_archivo), mode="a", encoding = 'utf-8')
salida = open(file='{}.out'.format(nombre_archivo), mode="w", encoding = 'utf-8')

for x in entrada:
    PrefixTree.leer_instrucciones(str(x).replace("\t", " "), salida)

entrada.close()
salida.close()

