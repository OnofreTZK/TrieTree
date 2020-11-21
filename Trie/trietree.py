from .node import Node

class Trie(object):

    # Construtor -----------------------------|
    def __init__( self ): #{{{

        self.root = Node('') # Nó raiz não terá nenhuma chave.

    #}}}
    # ----------------------------------------|

    def insert( self, word ):
        
        # O nó temporário será usado para verificar os filhos( as letras ja inseridas )
        temp_node = self.root
        
        for char in word:
            if char in temp_node.children:
                # Se ja houve um nó com essa letra, partiremos a partir dele.
                temp_node = temp_node.children[char]
            else:
                # Caso não haja um nó com essa letra
                # É criado um nó, será filho do nó atual
                # O nó temporário "avanća" para o novo nó
                new_node = Node(char)
                temp_node.children[char] = new_node
                temp_node = new_node

        # Ao fim do laćo, o nó atual é o fim da palavra.
        temp_node.is_end = True

