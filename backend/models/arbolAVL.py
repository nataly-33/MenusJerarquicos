class NodoMVias:
    """
    Representa un nodo de un árbol M-vías.

    Attributes:
        data (list): Lista de claves almacenadas en el nodo.
        hijos (list): Lista de hijos del nodo.
    """

    def __init__(self, dato):
        """
        Constructor del nodo M-vías.

        Args:
            dato: Primer dato que se insertará en el nodo.
        """
        self.data = [dato]  # Lista de claves ordenadas
        self.hijos = []  # Lista de hijos

    def esta_lleno(self, orden):
        """
        Verifica si el nodo está lleno.

        Args:
            orden (int): Orden del árbol.

        Returns:
            bool: True si el nodo está lleno, False en caso contrario.
        """
        return len(self.data) >= orden - 1

    def insertar_dato_ordenado(self, dato):
        """
        Inserta un dato de forma ordenada en el nodo.

        Args:
            dato: Dato a insertar.
        """
        self.data.append(dato)
        self.data.sort()

    def obtener_hijo(self, posicion):
        """
        Obtiene el hijo en una posición específica.

        Args:
            posicion (int): Índice del hijo a obtener.

        Returns:
            NodoMVias: El hijo en la posición dada o None si no existe.
        """
        if posicion < len(self.hijos):
            return self.hijos[posicion]
        return None

    def establecer_hijo(self, posicion, hijo):
        """
        Establece un hijo en la posición dada.

        Args:
            posicion (int): Índice donde se colocará el hijo.
            hijo (NodoMVias): Hijo que se insertará.
        """
        while len(self.hijos) <= posicion:
            self.hijos.append(None)
        self.hijos[posicion] = hijo

    def cantidad_datos_usados(self):
        """
        Retorna la cantidad de claves almacenadas en el nodo.

        Returns:
            int: Cantidad de claves.
        """
        return len(self.data)

    def __str__(self):
        """
        Representación en cadena del nodo.

        Returns:
            str: Las claves contenidas en el nodo.
        """
        return f"{self.data}"


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
            return  # El dato ya existe, no se inserta

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
                return -1  # El dato ya existe
            if dato < nodo.data[i]:
                return i  # Ir al hijo izquierdo
        return len(nodo.data)  # Ir al hijo más a la derecha

    def recorrido_inorden(self):
        """
        Muestra el recorrido inorden del árbol.
        """
        print("Menú en orden:")
        self._recorrido_inorden_recursivo(self.raiz)
        print()

    def _recorrido_inorden_recursivo(self, nodo):
        """
        Recorre el árbol en orden de manera recursiva.

        Args:
            nodo (NodoMVias): Nodo actual.
        """
        if nodo is not None:
            cantidad = len(nodo.data)
            for i in range(cantidad):
                if i < len(nodo.hijos):
                    self._recorrido_inorden_recursivo(nodo.hijos[i])
                print(nodo.data[i], end="  ")
            if len(nodo.hijos) > cantidad:
                self._recorrido_inorden_recursivo(nodo.hijos[cantidad])

    def mostrar_niveles(self):
        """
        Muestra los nodos del árbol por niveles.
        """
        if self.raiz is None:
            print("Árbol vacío")
            return

        print("Menú por niveles:")
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


# Ejemplo de uso
if __name__ == "__main__":
    arbol = ArbolMVias(4)

    arbol.insertar("1 General")
    arbol.insertar("2 Seguridad")
    arbol.insertar("3 Usuario")
    arbol.insertar("1.1 Logs")
    arbol.insertar("2.1 Contraseña")
    arbol.insertar("1.2 Configuración")
    arbol.insertar("3.1 Inicio")

    arbol.recorrido_inorden()
    arbol.mostrar_niveles()
