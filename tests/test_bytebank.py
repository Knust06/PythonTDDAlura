from bytebank import Funcionario
import pytest
from pytest import mark


class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_24(self):
        entrada = '13/03/2000'  #Given-Contexto
        esperado = 24

        funcionario_teste = Funcionario('Teste', entrada, 1111)

        resultado = funcionario_teste.idade()  #When-Ação

        assert resultado == esperado  #Then-Desfecho

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        entrada = 'Lucas Carvalho'
        esperado = 'Carvalho'

        funcionario_teste = Funcionario(entrada, '13/03/2000', 1111)
        resultado = funcionario_teste.sobrenome()
        assert resultado == esperado

    #@mark.skip
    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '13/03/2000', entrada_salario)
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_Bonus(self):
        entrada_salario = 1000
        esperado = 100

        funcionario_teste = Funcionario('Teste', '13/03/2000', entrada_salario)
        resultado = funcionario_teste.calcular_bonus()

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada_salario = 1000000

            funcionario_teste = Funcionario('Teste', '13/03/2000', entrada_salario)
            resultado = funcionario_teste.calcular_bonus()

            assert resultado

    #def test_retorno_str(self):
        #nome, data_nascimento, salario = 'Teste', '13/03/2000', 1000
        #esperado = 'Funcionario(Teste, 13/03/2000, 1000)'

        #funcionario_teste = Funcionario(nome, data_nascimento, salario)
        #resultado = funcionario_teste.__str__()

        #assert resultado == esperado