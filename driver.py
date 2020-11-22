from Trie import *

tree = Trie()

# Inserções ---------------------------------------------------
tree.insert("Porto")
tree.insert("Paris")
tree.insert("Ma")
tree.insert("Manaus")
tree.insert("Madrid")
tree.insert("Barcelona")

# ------------------------------------------------------------
#print( tree.root.children.keys() )


# Buscas -----------------------------------------------------
tree.search("Porto")
tree.search("Paris")
tree.search("Ma")
tree.search("Manaus")
tree.search("Madrid")
tree.search("Barcelona")
tree.search("Bahia")
# ------------------------------------------------------------
# Esta ultima busca deve retornar não encontrada!!

# Teste manual -----------------------------------------------
insert_word = input("\nInsira uma palavra na árvore:\n")

tree.insert(insert_word)

search_word = input("\nInsira a palavra que deseja procurar:\n")
tree.search(search_word)
# ------------------------------------------------------------
