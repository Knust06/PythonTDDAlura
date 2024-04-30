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
