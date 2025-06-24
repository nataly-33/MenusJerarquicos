from models.NodoMvias import NodoMVias

class ArbolMVias:
    """
    Representa un árbol M-vías.

    Attributes:
        raiz (NodoMVias): Nodo raíz del árbol.
        orden (int): Orden del árbol.
    """

    def __init__(self, orden):
        """
        Constructor del árbol M-vías.

        Args:
            orden (int): Orden del árbol (máximo número de hijos por nodo).
        """
        self.raiz = None
        self.orden = orden

    def insertar(self, dato):
        """
        Inserta un nuevo dato en el árbol.

        Args:
            dato: Dato que se insertará.
        """
        if not self.raiz:
            self.raiz = NodoMVias(dato)
        else:
            self._insertar_recursivo(self.raiz, dato)

    def _insertar_recursivo(self, nodo, dato):
        """
        Inserta un dato de forma recursiva en el árbol.

        Args:
            nodo (NodoMVias): Nodo actual donde se evalúa la inserción.
            dato: Dato que se insertará.
        """
        if not nodo.esta_lleno(self.orden):
            nodo.insertar_dato_ordenado(dato)
            return

        posicion = self._hijo_descendente(nodo, dato)

        if posicion == -1:
            return  

        hijo = nodo.obtener_hijo(posicion)

        if hijo is None:
            nuevo_hijo = NodoMVias(dato)
            nodo.establecer_hijo(posicion, nuevo_hijo)
        else:
            self._insertar_recursivo(hijo, dato)

    def _hijo_descendente(self, nodo, dato):
        """
        Determina hacia qué hijo debe continuar la inserción.

        Args:
            nodo (NodoMVias): Nodo actual.
            dato: Dato que se desea insertar.

        Returns:
            int: Índice del hijo donde debe continuar la inserción.
                 Retorna -1 si el dato ya existe.
        """
        for i in range(len(nodo.data)):
            if dato == nodo.data[i]:
                return -1 
            if dato < nodo.data[i]:
                return i  
        return len(nodo.data)  

    def mostrar_niveles(self):
        """
        Muestra los nodos del árbol por niveles.
        """
        if self.raiz is None:
            print("Árbol vacío")
            return

        print("Organizado por niveles:")
        cola = [(self.raiz, 0)]
        nivel_actual = -1

        while cola:
            nodo, nivel = cola.pop(0)

            if nivel != nivel_actual:
                print(f"\nNivel {nivel}: ", end="")
                nivel_actual = nivel

            print(nodo, end="  ")

            for hijo in nodo.hijos:
                if hijo is not None:
                    cola.append((hijo, nivel + 1))

        print()
    
    def obtener_niveles(self):
        """
        Devuelve la estructura del árbol por niveles en formato JSON, como una lista de listas.

        Returns:
            list: Lista de niveles, cada nivel es una lista de nodos.
        """
        if self.raiz is None:
            return []

        niveles = []
        cola = [(self.raiz, 0)]

        while cola:
            nodo, nivel = cola.pop(0)

            if nivel >= len(niveles):
                niveles.append([])

            niveles[nivel].append(nodo.data)

            for hijo in nodo.hijos:
                if hijo is not None:
                    cola.append((hijo, nivel + 1))

        return niveles
    
"""
if __name__ == "__main__":
    arbol = ArbolMVias(4)

    arbol.insertar("1 General")
    arbol.insertar("2 Seguridad")
    arbol.insertar("3 Usuario")
    arbol.insertar("1.1 Logs")
    arbol.insertar("2.1 Contraseña")
    arbol.insertar("1.2 Configuración")
    arbol.insertar("3.1 Inicio")
    arbol.insertar("0 Utilidades")


    arbol.mostrar_niveles()
    json_menu = arbol.obtener_json()
    print("\nMenú en formato JSON:")
    print(json_menu)
"""