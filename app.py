from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante("praça", "gourmet")
bebida_suco = Bebida("Suco de Melancia", 5, "Grande")
prato_paozinho = Prato("Pãozinho", 2, "O melhor pão da cidade")


def main():
    print(bebida_suco)

if __name__ == "__main__":
    main()