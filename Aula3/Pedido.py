from Categoria import Categoria
from Produto import Produto

class Pedido:
    def __init__(self, end):
        
        self.id = None
        self.endereco = end
        self.produtos = []
        

    #def addProd(prod:Produto) double
    # método addProd receberá um objeto do tipo Produto e adicione na lista de produtos existente no atributo
    #produtos da Classe Pedido, retornando o total do Pedido

    def addProd(self, prod):
        self.produtos.append(prod)
        total = 0.0
        for produto in self.produtos:
            total += produto.preco
        return total


# Exemplo de uso
cat_alimentos = Categoria("Alimentos")
prod1 = Produto("Arroz", 5.99, cat_alimentos)
prod2 = Produto("Feijão", 3.49, cat_alimentos)
prod3 = Produto("Macarrão", 2.19, cat_alimentos)

endereco_entrega = "Rua ABC, 123"
pedido = Pedido(endereco_entrega)
total_pedido = pedido.addProd(prod1)  # Adicionar produtos ao pedido
total_pedido = pedido.addProd(prod2)
total_pedido = pedido.addProd(prod3)

print("Total do pedido:", total_pedido)