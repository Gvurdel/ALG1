
from Carro import Carro
from Drone import Drone
from FilaVeiculos import FilaVeiculos

def menu():
    fila_carros = FilaVeiculos()
    fila_drones = FilaVeiculos()

    while True:
        print("\nMENU:")
        print("1. Adicionar Carro")
        print("2. Remover Carro")
        print("3. Adicionar Drone")
        print("4. Remover Drone")
        print("5. Imprimir Fila de Carros")
        print("6. Imprimir Fila de Drones")
        print("7. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            marca = input("Digite a marca do carro: ")
            modelo = input("Digite o modelo do carro: ")
            portas = input("Digite a quantidade de portas do carro: ")
            carro = Carro(marca, modelo, portas)
            fila_carros.adicionar_veiculo(carro)
        elif escolha == "2":
            fila_carros.remover_veiculo()
        elif escolha == "3":
            marca = input("Digite a marca do drone: ")
            modelo = input("Digite o modelo do drone: ")
            helices = input("Digite a quantidade de hélices do drone: ")
            drone = Drone(marca, modelo, helices)
            fila_drones.adicionar_veiculo(drone)
        elif escolha == "4":
            fila_drones.remover_veiculo()
        elif escolha == "5":
            fila_carros.imprimir_fila()
        elif escolha == "6":
            fila_drones.imprimir_fila()
        elif escolha == "7":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
