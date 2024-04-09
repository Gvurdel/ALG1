#metodo que não recebe parâmetro e possui retonro

def getPI():
    return 3.14

def getDobroDoPI():
    return getPI() * 2

#metodo que não recebe parâmetro e não possui retorno

def imprimirPI():
    print(getPI())

#metodo que recebe parâmetro e possui retorno

def getAreaCirculo(raio):
    return getPI() * (raio * raio)

#metodo que recebe parâmetro e não possui retorno

def imprimirAreaCirculo(raio):
    print(getAreaCirculo(raio))

#execução

imprimirPI()

print(getAreaCirculo(6 * 2))

imprimirAreaCirculo(10)

