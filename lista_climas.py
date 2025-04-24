from nodo import NodoLetra

class ListaDeListas:
    def __init__(self):
        self.cabeza = None

    def agregar_letra(self, letra, climas):
        nuevo_nodo = NodoLetra(letra)
        for clima in climas:
            nuevo_nodo.agregar_clima(clima)

        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def consultar_clima(self, ciudad, hora):
        actual_letra = self.cabeza
        while actual_letra:
            if actual_letra.letra.lower() == ciudad.lower():
                if isinstance(actual_letra.lista_climas, dict):
                    return actual_letra.lista_climas
                actual_clima = actual_letra.lista_climas
                contador = 0
                while actual_clima:
                    if contador == hora % len(self.obtener_climas(actual_letra)):
                        clima = actual_clima.clima
                        if clima == "Soleado" and (hora < 6 or hora >= 18):
                            clima = "Despejado"
                        return f"A las {hora:02d}:00 en {ciudad}, el clima será {clima}."
                    actual_clima = actual_clima.siguiente
                    contador += 1
                return "No hay clima para esa hora."
            actual_letra = actual_letra.siguiente
        return "Ciudad no encontrada."

    def obtener_climas(self, nodo_letra):
        climas = []
        actual_clima = nodo_letra.lista_climas
        while actual_clima:
            climas.append(actual_clima.clima)
            actual_clima = actual_clima.siguiente
        return climas
