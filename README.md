# Web Scraper para Extração de Links

Este script utiliza Selenium para acessar um site e extrair informações sobre os links presentes na página. Os dados extraídos são salvos em um arquivo Excel utilizando a biblioteca `pandas` e `openpyxl`.

## Funcionalidade

- Configura o WebDriver para o Chrome.
- Acessa uma URL especificada.
- Extrai o título da página e o texto do primeiro elemento `<h1>`.
- Encontra todos os links (`<a>` tags) na página.
- Salva o texto dos links e suas URLs em um arquivo Excel.

## Requisitos

Antes de executar o script, certifique-se de ter as seguintes bibliotecas instaladas:

- `selenium`
- `webdriver_manager`
- `pandas`
- `openpyxl`

Você pode instalar as dependências necessárias usando o `pip`:

```bash
pip install selenium webdriver-manager pandas openpyxl
```

## Configuração
URL do Site: No script, substitua '' pela URL do site que você deseja acessar.

```bash
driver.get('https://exemplo.com')
```
Salvar Dados: O script salva os dados em um arquivo chamado dados_links.xlsx no mesmo diretório onde o script é executado.

Como Usar
Clone este repositório para o seu ambiente local:

```bash
Copiar código
git clone <URL-DO-REPOSITORIO>
cd <NOME-DO-REPOSITORIO>
```
Execute o script:

```bash
python nome_do_script.py
```
Certifique-se de substituir nome_do_script.py pelo nome real do arquivo Python.
