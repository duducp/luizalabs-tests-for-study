from par_ou_impar import jogar
from typing import Callable
from time import sleep
from magatest.mock import MagicMock, patch, parametrize
import par_ou_impar
from unittest import mock as unittest_mock


@parametrize('choice,value', [
    ('par', 2),
    ('impar', 3),
    ('par', 4),
    ('impar', 5),
])
def test_par_ou_impar_should_win(choice, value):
    with patch('par_ou_impar.random') as mock_random:
        mock_random.randint.return_value = 2

        assert jogar(choice, value)
        assert mock_random.randint.call_count == 1
        mock_random.randint.assert_called()
        mock_random.randint.assert_called_with(0, b=10)


def test_magic_mock_instance():
    mock = MagicMock()

    soma_mock = mock.soma
    soma_mock.value = 2

    assert isinstance(soma_mock, MagicMock)
    assert soma_mock is mock.soma
    assert soma_mock.value == 2


def test_jogador():
    with unittest_mock.patch(
        'par_ou_impar.Jogador.jogou', 
        return_value=False
    ):
        assert not par_ou_impar.jogador_jogou()
