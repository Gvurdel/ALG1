# Listas de produtos, preços e quantidades
nomes_produtos = ["Produto 1", "Produto 2", "Produto 3"]
precos = [10.99, 20.49, 5.99]
quantidades = [5, 3, 10]

def imprimir_produto(indice):
    if 0 <= indice < len(nomes_produtos):
        print("Produto:", nomes_produtos[indice])
        print("Preço:", precos[indice])
        print("Quantidade:", quantidades[indice])
    else:
        print("Índice inválido!")

def retirar_produto(indice):
    if 0 <= indice < len(nomes_produtos):
        nomes_produtos.pop(indice)
        precos.pop(indice)
        quantidades.pop(indice)
        print("Produto removido com sucesso!")
    else:
        print("Índice inválido!")

while True:
    print("\nMenu:")
    print("1. Imprimir informações de um produto")
    print("2. Retirar um produto")
    print("3. Sair")
    
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        indice = int(input("Digite o índice do produto: "))
        imprimir_produto(indice)
    elif escolha == "2":
        indice = int(input("Digite o índice do produto a ser removido: "))
        retirar_produto(indice)
    elif escolha == "3":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Por favor, escolha novamente.")
