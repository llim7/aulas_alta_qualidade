from abc import ABC, abstractmethod

class Desconto(ABC):
    @abstractmethod
    def calcular(self, valor):
        pass

class DescontoNormal(Desconto):
    def calcular(self, valor):
        return valor * 0.1

class DescontoVIP(Desconto):
    def calcular(self,valor):
        return valor * 0.2

class DescontoPremium(Desconto):
    def calcular(self, valor):
        return valor * 0.3

def main():

    valor = 100

    normal = DescontoNormal()
    vip = DescontoVIP()
    premium = DescontoPremium()

    print(f"Desconto Normal: R${normal.calcular(valor):.2f}")
    print(f"Desconto VIP: R${vip.calcular(valor):.2f}")
    print(f"Desconto Premiumn: R${premium.calcular(valor):.2f}")

if __name__ == "__main__":
    main()