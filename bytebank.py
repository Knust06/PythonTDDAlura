from datetime import date

class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    def idade(self):
        data_nascimento_quebrada = self._data_nascimento.split('/')
        ano_nascimento = data_nascimento_quebrada[-1]
        ano_atual = date.today().year
        return ano_atual - int(ano_nascimento)

    def sobrenome(self):
        nome_completo = self.nome.strip()
        nome_quebrado = nome_completo.split(' ')
        return nome_quebrado[-1]

    def _eh_socio(self):
        sobrenomes = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']
        return self._salario >= 100000 and self.sobrenome() in sobrenomes
    def decrescimo_salario(self):
        if self._eh_socio():
            decrescimo = self.salario * 0.1
            self._salario = self._salario - decrescimo

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            raise Exception('O salário é muito alto para receber um bônus')
        return valor

    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'

    #pytest --cov Para ver a cobertura dos testes
    #pytest --cov=tests/            para ver a cobertura de testes em um lugar especifico
    #pytest -v -m calcular_bonus -v        para ser verboso e -m para marcar que quero usar um marcador
    #pytest --cov=tests/ --cov-report term-missing    mostra a linha que esta faltando os testes
    #pytest --cov=bytebank --cov-report term-missing  mostra a linha que esta faltando os testes
    #pytest --cov=bytebank --cov-report html      Criando pagina web para ver os testes
    #pytest --junitxml report.xml
    #pytest --cov-report xml