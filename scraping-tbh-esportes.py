from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager 
import pandas as pd

from time import sleep

website = 'https://www.tbhesportes.com.br/eventos-2023/' 
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) 
driver.get(website) 

driver.maximize_window() 

linhas_corridas = driver.find_elements('xpath', '//article//div[@class="postcontent"]/div/div[@class="inner-flex"]')

# Extrair text, alt e href de cada item da lista
meses = []
corridas = []
links = []
for lista in linhas_corridas:
    for item in lista.find_elements('xpath', './div'):
        if item.text == '':
            try:
                descricao_corrida = item.find_element('xpath', './/img').get_attribute('alt')
                link_corrida = item.find_element('xpath', './/a').get_attribute('href') 
                print(link_corrida, descricao_corrida)

                meses.append(mes)
                corridas.append(descricao_corrida)
                links.append(link_corrida)
                continue
            except: 
                continue  
        mes = item.text
        
        # print(item.find_element('xpath',  '//text()'))

df = pd.DataFrame({'mes': meses, 'corrida': corridas, 'link': links})
df.to_csv('tbh-esportes.csv', index=False)
sleep(10)

