from bytebank import Funcionario


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

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '13/03/2000', entrada_salario)
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        assert resultado == esperado

    def test_quando_calcular_bonus_recebe_1000_deve_retornar_Bonus(self):
        entrada_salario = 1000
        esperado = 100

        funcionario_teste = Funcionario('Teste', '13/03/2000', entrada_salario)
        resultado = funcionario_teste.calcular_bonus()

        assert resultado == esperado

