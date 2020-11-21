
class Node(object):
    
    # Construtor -----------------------------|
    def __init__( self, key ): #{{{

        self.char = key # A chave será a letra
        self.is_end = False # Verifica se o nó é o final da palavra.
        self.children = {} # Dicionário( Chaves = Letras, Valores = Nós )

    #}}}
    # ----------------------------------------|

