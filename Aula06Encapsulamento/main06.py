from Conta import Conta

c = Conta()

c.saldo = 1.0

print(c.getSaldo())

c.depositar(50.0)

print(c.saldo)

c.sacar(5)

print(c.saldo)