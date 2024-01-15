from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

servico = ChromeService(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

time.sleep(5)
#entra no link
navegador.get("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
#acha o form do email pelo xpath e ainda digita pelo send_keys
navegador.find_element('xpath', '//*[@id="email"]').send_keys('testaai@gmail.com')
#acha o form da senha pelo xpath e ainda digita pelo send_keys
navegador.find_element('xpath', '//*[@id="password"]').send_keys('senhaqualquer')
#acha o botao pelo xpath e ainda clica
navegador.find_element('xpath', '//*[@id="pgtpy-botao"]').click()

#agora ele cai em outra pagina!

base = pd.read_csv("produtos.csv")

# completo = base.index
# 50 itens = range(0, 50)

for linha in base.index:
    #preenchendo os campos!
    navegador.find_element('xpath', '//*[@id="codigo"]').send_keys(base.loc[linha, 'codigo'])
 
    navegador.find_element('xpath', '//*[@id="marca"]').send_keys(base.loc[linha, 'marca'])

    navegador.find_element('xpath', '//*[@id="tipo"]').send_keys(base.loc[linha, 'tipo'])
 
    navegador.find_element('xpath', '//*[@id="categoria"]').send_keys(str(base.loc[linha, 'categoria']))

    navegador.find_element('xpath', '//*[@id="preco_unitario"]').send_keys(str(base.loc[linha, 'preco_unitario']))

    navegador.find_element('xpath', '//*[@id="custo"]').send_keys(str(base.loc[linha, 'custo']))

    if not pd.isna(base.loc[linha, 'obs']):
        navegador.find_element('xpath', '//*[@id="obs"]').send_keys(base.loc[linha, 'obs'])    
    
    while True:

        checkbox = navegador.find_element('xpath', '//*[@id="codigo"]').get_attribute("value")

        if checkbox != '':
            navegador.find_element('xpath', '//*[@id="pgtpy-botao"]').click()
        else:
            break

time.sleep(10)