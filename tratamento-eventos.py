import pandas as pd 
import json

resultados = "https://webservices.esferabr.com.br/Ativo/ResultadoComFotos?id_evento="
eventos = pd.read_csv('resultados_ativo/data_scraped/eventos.csv')
eventos_o2_bh = (
    eventos
    .query('organizador == "O2Corre" and cidade == "Belo Horizonte" and tipo_evento == "Corrida de Rua" and data > "2022-01-01"')
)

# print(eventos_o2_bh)

link_resultados = []
for id in eventos_o2_bh['id_evento']:
    link_resultados.append(resultados + str(id) + '&offset=0')

with open("resultados_ativo/resultados_ativo/spiders/links_resultados.json", 'w') as f:
    json.dump(link_resultados, f)