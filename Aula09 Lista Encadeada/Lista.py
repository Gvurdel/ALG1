from No import No

class Lista:
    
    def __init__(self):
        self.primeiro = None
        self.tamanho = 0
        
    def addNoInicio(self, valor):
        no = No(valor)
        if self.primeiro == None:
            self.primeiro = no
            
        else:
            no.proximo = self.primeiro
            self.primeiro = no
            
        self.tamanho += 1
        self.imprimir()
        
    def imprimir(self):
        aux = self.primeiro
        while(aux):
            print(aux.dado)
            aux = aux.proximo
        print("Total: " , self.tamanho)
        
    def addNoFim(self, valor):
        no = No(valor)
        if self.primeiro == None:
            self.primeiro = no
            
        else:
            aux = self.primeiro
            while(aux):
                if aux.proximo == None:
                    aux.proximo = no
                    break
                aux = aux.proximo
        self.tamanho += 1
        self.imprimir()
        
    def removerDoinicio(self):
        if self.primeiro == None:
            print("Lista Vazia!")
        elif self.primeiro.proximo == None:
            self.primeiro = None
            self.tamanho = 0
        else:
            self.primeiro = self.primeiro.proximo
            self.tamanho -= 1
        self.imprimir()   
            
            