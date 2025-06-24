class NodoMVias:
    """
    Representa un nodo de un árbol M-vías.

    Attributos:
        data (list): Lista de claves almacenadas en el nodo.
        hijos (list): Lista de hijos del nodo.
    """

    def __init__(self, dato):
        """
        Constructor del nodo M-vías.

        Args:
            dato: Primer dato que se insertará en el nodo.
        """
        self.data = [dato] 
        self.hijos = []  

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