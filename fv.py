livros = []

def adicionar_livro(nome_livro):
    # cada livro será armazenado como um array (lista)
    livro = [nome_livro]
    livros.append(livro)

# Testando a função
adicionar_livro("Dom Casmurro")
adicionar_livro("O Pequeno Príncipe")

print(livros)