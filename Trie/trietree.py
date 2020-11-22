from .node import Node

class Trie(object):

    # Construtor ---------------------------------------------|
    def __init__( self ): #{{{

        self.root = Node('') # Nó raiz não terá nenhuma chave.

    #}}}
    # --------------------------------------------------------|

    def insert( self, word ): #{{{

        # O nó temporário será usado para verificar os filhos( as letras ja inseridas ).
        temp_node = self.root

        for char in word.lower():
            if char in temp_node.children:
                # Se ja houver um nó com essa letra, partiremos a partir dele.
                temp_node = temp_node.children[char]
            else:
                # Caso não haja um nó com essa letra
                # É criado um nó, este será o filho do nó atual.
                # O nó temporário "avança" para o novo nó.
                new_node = Node(char)
                temp_node.children[char] = new_node
                temp_node = new_node

        # Ao fim do laço, o nó atual é o fim da palavra.
        temp_node.is_end = True

    #}}}


    def search( self, word ): #{{{

        word = word.lower()

        # Nó temporário que irá percorrer a árvore.
        temp_node = self.root

        # index da string word.
        idx = 0

        # String que armazenará cada letra pra verificar a corretude da buscar.
        final_word = ""

        # Laço que deve parar no ultimo nó após finalizada a busca.
        for char in range( len(word) ):
            # Primeiro condição: a letra atual está na lista de filhos do nó atual
            if word[idx] in temp_node.children:
                # O nó atual avança para o nó da letra achada.
                temp_node = temp_node.children[ word[idx] ]
                # Insere a letra na string de corretude.
                final_word = final_word + temp_node.char
                # Incrementa o index
                idx += 1
            else:
                print("------------------------------------------")
                print("Palavra procurada: " + word )
                print("A palavra: " + word + " não foi encontrada!")
                print("------------------------------------------")
                return False

        print("------------------------------------------")
        print("Palavra procurada " + word + "\nPalavra encontrada: " + final_word )
        print("------------------------------------------")

        # Ao fim do laço, o nó atual deve ser o fim da palavra.
        return temp_node.is_end

    #}}}





