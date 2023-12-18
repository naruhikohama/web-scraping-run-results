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

for linha in linhas_atletas:
    print(linha.text)

