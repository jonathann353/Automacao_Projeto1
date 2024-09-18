from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import openpyxl
import pandas as pd

# Configura o WebDriver para o Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Acessa o site
driver.get('https://exemplo.com')

# Aguarda a página carregar (opcional, útil se o site for lento)
driver.implicitly_wait(10)

# Exemplo: Extrair o título da página
titulo = driver.title
print(f"Título da página: {titulo}")

# Exemplo: Encontrar elementos na página por seletor (h1)
elemento_h1 = driver.find_element(By.TAG_NAME, 'h1').text
print(f"Texto do H1: {elemento_h1}")

# Encontrar todos os links (<a> tags)
links = driver.find_elements(By.TAG_NAME, 'a')

# Criar listas para armazenar os dados
lista_texto_links = []
lista_urls = []

# Percorre todos os links e extrai texto e URL
for link in links:
    texto = link.text.strip()
    url = link.get_attribute('href')
    
    # Adiciona apenas se o link e o texto não forem vazios
    if texto and url:
        lista_texto_links.append(texto)
        lista_urls.append(url)

# Criando o DataFrame com os links e textos extraídos
data = {
    'Texto do Link': lista_texto_links,
    'URL': lista_urls
}

df = pd.DataFrame(data)

# Salvando o DataFrame em um arquivo Excel
df.to_excel('dados_links.xlsx', index=False)

print("Dados salvos com sucesso no arquivo 'dados_links.xlsx'")

# Fecha o navegador
driver.quit()
