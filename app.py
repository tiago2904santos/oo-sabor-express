from modelos.restaurante import Restaurante

restaurante_praca = Restaurante("praça", "gourmet")
restaurante_praca.receber_avaliacao("Tiago", 3)
restaurante_praca.receber_avaliacao("Julia", 9)


def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()