from nodo_clima import NodoClima

class NodoLetra:
    def __init__(self, letra):
        self.letra = letra
        self.lista_climas = None
        self.siguiente = None

    def agregar_clima(self, clima):
        nuevo_clima = NodoClima(clima)
        if not self.lista_climas:
            self.lista_climas = nuevo_clima
        else:
            actual = self.lista_climas
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_clima