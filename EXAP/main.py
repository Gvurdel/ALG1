from Torre import Torre 
from Apartamento import Apartamento
from FilaEspera import FilaEspera
from ApComVaga import ApComVaga

lista_torres = []
lista_apartamentos = []

torre1 = Torre(1, "Torre A", "Endereço A")
torre2 = Torre(2, "Torre B", "Endereço B")

ap1 = Apartamento(1, "101", torre1, None)
ap2 = Apartamento(2, "102", torre2, None)
ap3 = Apartamento(3, "103", torre1, None)

lista_filaEspera = FilaEspera()
lista_ApComVaga = ApComVaga()

lista_filaEspera.adicionar_apartamento(ap2)
lista_filaEspera.adicionar_apartamento(ap3)
lista_filaEspera.adicionar_apartamento(ap1)



torre1.imprimir()
torre2.imprimir()

ap1.imprimir()

# Imprimir apartamentos com vaga
print("\nApartamentos com vaga:")
lista_ApComVaga.imprimir_lista()

print("\nRetirar apartamento da fila de espera e atribuir vaga")
ap_retirado = lista_filaEspera.retirar_apartamento(4)
if ap_retirado:
    lista_ApComVaga.adicionar_apartamento(ap_retirado)

# Imprimir fila de espera
print("\nFila de espera:")
lista_filaEspera.imprimir_fila()

print("\nRetirar apartamento da fila de espera e atribuir vaga")
ap_retirado = lista_filaEspera.retirar_apartamento(2)
if ap_retirado:
    lista_ApComVaga.adicionar_apartamento(ap_retirado)

# Imprimir apartamentos com vaga após retirada da fila de espera
print("\nApartamentos com vaga após retirada da fila de espera:")
lista_ApComVaga.imprimir_lista()

