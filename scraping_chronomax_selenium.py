from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

import pandas as pd 
from time import sleep 

df = (
    pd.read_csv('chronomax_runs_tratado.csv')
    .assign(
        link = lambda dff: dff['link'].str.replace(";", ""),
    )
)

links = df['link'].tolist()

corrida = df['prova'].tolist()[0].replace(" ", "_").lower()
link_1 = links[0]

print(link_1)

website = link_1
options = Options()
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(website)
driver.maximize_window()


sleep(3)
count = 0
while count < 3:
    driver.execute_script("document.getElementById('divGr').scrollTop += 5000")
    sleep(2)
    count += 1

linhas_atletas = driver.find_elements('xpath', '//table[@id="tabres"]//tbody//tr')

posicao = []
num_peito = []
nome = []
equipe = []
sexo = []
categoria = []
pos_categoria = []
parcial_1 = []
parcial_2 = []
tempo_liquido = []
tempo_bruto = []
pace_medio = []
for linha in linhas_atletas:
    posicao.append(linha.find_element('xpath', './td[1]').text)
    num_peito.append(linha.find_element('xpath', './td[2]').text)
    nome.append(linha.find_element('xpath', './td[3]').text)
    equipe.append(linha.find_element('xpath', './td[4]').text)
    sexo.append(linha.find_element('xpath', './td[5]').text)
    categoria.append(linha.find_element('xpath', './td[6]').text)
    pos_categoria.append(linha.find_element('xpath', './td[7]').text)
    parcial_1.append(linha.find_element('xpath', './td[8]').text)
    parcial_2.append(linha.find_element('xpath', './td[9]').text)
    tempo_liquido.append(linha.find_element('xpath', './td[10]').text)
    tempo_bruto.append(linha.find_element('xpath', './td[11]').text)
    pace_medio.append(linha.find_element('xpath', './td[12]').text)

df = pd.DataFrame({
    'posicao': posicao,
    'num_peito': num_peito,
    'nome': nome,
    'equipe': equipe,
    'sexo': sexo,
    'categoria': categoria,
    'pos_categoria': pos_categoria,
    'parcial_1': parcial_1,
    'parcial_2': parcial_2,
    'tempo_liquido': tempo_liquido,
    'tempo_bruto': tempo_bruto,
    'pace_medio': pace_medio,
})

df.to_csv(f'chronomax_resultados/chronomax_{corrida}.csv', index=False)

