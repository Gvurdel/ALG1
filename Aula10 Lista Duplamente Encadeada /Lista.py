from No import No

class Lista:
    
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
        
    def add(self, valor):
        nodo = No(valor)
        if self.inicio == None:
            self.inicio = nodo
            self.fim = nodo
        else:
            if nodo.dado < self.inicio.dado:
                nodo.proximo = self.inicio
                self.inicio.anterior = nodo
                self.inicio = nodo
            else:
                ant = self.inicio
                aux = self.inicio.proximo
                while aux != None :
                    if nodo.dado < aux.dado:
                        nodo.proximo = ant.proximo   
                        ant.proximo = nodo
                        nodo.anterior = ant
                        aux.anterior = nodo
                        break
                    else: 
                        ant = aux
                        aux = aux.proximo
                if aux == None and nodo.dado >= ant.dado:
                    ant.proximo = nodo
                    nodo.anterior = ant
                    self.fim = nodo

                    
        self.tamanho += 1
        self.imprimir()
                            
    def imprimir(self):
        print("---------------------")
        if self.inicio == None:
            print("Lista Vazia!")
        else:
            aux = self.inicio
            while aux :
                print( aux.dado )
                aux = aux.proximo
            print( "Tamanho: ", str(self.tamanho))

    def imprimirReverso(self):
        print("---------------------")
        if self.fim == None:
            print("Lista Vazia!")
        else:
            aux = self.fim
            while aux :
                print( aux.dado )
                aux = aux.anterior
            print( "Tamanho: ", str(self.tamanho))
            
    def remover(self, valor):
        tamAtual = self.tamanho
        if self.inicio == None:
            print("Lista Vazia")
            
            # Lista contendo só um elemento
            # e este é igual ao valor
        elif self.inicio.proximo == None and self.inicio.dado == valor:
            self.inicio = None
            self.fim = None
            self.tamanho = 0
        else:
            # Lista contendo vários elementos e o valor é igual ao primeiro
            if self.inicio.dado == valor:
                self.inicio.proximo.anterior = None
                self.inicio = self.inicio.proximo
                self.tamanho -= 1
            # Lista com vários elementos e o valor não está no primeiro    
            else:
                ant = self.inicio
                aux = self.inicio.proximo
                while aux :
                    if aux.dado == valor:
                        ant.proximo = aux.proximo
                        if aux.proximo == None:
                            self.fim = ant
                        else:
                            aux.proximo.anterior = ant
                        self.tamanho -= 1
                        break
                    else:
                        ant = aux
                        aux = aux.proximo
        if tamAtual == self.tamanho:
            print("Valor não encontrado")
        self.imprimir()
                
                
            