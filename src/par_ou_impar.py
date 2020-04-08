from random import randint


class Jogador:
    def jogou(self):
        return True


def jogador_jogou() -> bool:
    return Jogador().jogou()


def jogar(opcao: str, numero:int) -> bool:
    numero_do_computador = randint(0, 10)

    total = numero + numero_do_computador

    if total % 2 == 0 and opcao == 'par':
        return True
    elif total % 2 == 1 and opcao == 'impar':
        return True

    return False
