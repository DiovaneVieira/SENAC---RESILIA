class Nodo:
    """Esta classe representa um nodo de uma estrutura duplamente encadeada."""
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)


class Fila:
    """Esta classe representa uma fila usando uma estrutura encadeada."""

    def __init__(self):
        self.primeiro = None
        self.ultimo   = None


    def __repr__(self):
        return "[" + str(self.primeiro) + "]"