
# Python e TDD: Explorando Testes Unitários

Este projeto demonstra a aplicação de Test Driven Development (TDD) em Python. O projeto consiste em uma aplicação simples que simula operações bancárias.

## Estrutura do Projeto

- `bytebank.py`: Contém a lógica do negócio para as operações bancárias.
- `main.py`: Ponto de entrada da aplicação, onde as funções definidas em `bytebank.py` são utilizadas.
- `tests`: Diretório que contém todos os testes unitários escritos para garantir a funcionalidade do projeto.

## Configuração

Para rodar este projeto, você precisará de Python 3.8 ou superior. É recomendável usar um ambiente virtual para instalar as dependências.

### Configurando o ambiente virtual

1. Clone o repositório.
2. Navegue até o diretório do projeto.
3. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   ```
4. Ative o ambiente virtual:
   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - Unix ou MacOS:
     ```bash
     source venv/bin/activate
     ```
5. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Executando os Testes

Para executar os testes, use o seguinte comando:

```bash
pytest
```

## Ferramentas de Teste

- `Pytest`: Usado para rodar os testes unitários.
- `coverage.py`: Ferramenta para medir a cobertura dos testes.

## Gerando Relatórios de Cobertura

Para gerar um relatório de cobertura, execute:

```bash
coverage run -m pytest
coverage report
```

Ou, para gerar um relatório em HTML:

```bash
coverage html
```

Isso criará uma pasta `htmlcov` com os relatórios de cobertura em formato HTML.

## Contribuições

Contribuições são sempre bem-vindas. Certifique-se de escrever testes para novas funcionalidades ou correções.
