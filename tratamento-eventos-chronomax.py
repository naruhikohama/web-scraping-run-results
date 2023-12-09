import pandas as pd 
from numpy import where

eventos = pd.read_csv('chronomax_runs.csv')

mes = {
    "JAN": "01",
    "FEV": "02",
    "MAR": "03",
    "ABR": "04",
    "MAI": "05",
    "JUN": "06",
    "JUL": "07",
    "AGO": "08",
    "SET": "09",
    "OUT": "10",
    "NOV": "11",
    "DEZ": "12"
}

eventos_chronomax = (
    eventos
    .assign(
        ano = lambda dff: dff['data'].str.split("-").str[0],
        mes = lambda dff: dff['data'].str.split("-").str[1].map(mes),
        dia = lambda dff: dff['data'].str.split("-").str[2],
        # mes = lambda dff: dff['mes'].map(mes),
        data_tratada = lambda dff: dff['ano'] + "-" + dff['mes'] + "-" + dff['dia'],
        data = lambda dff: pd.to_datetime(dff['data_tratada']),
        prova = lambda dff: dff['prova'].str.upper(),
        local_upper = lambda dff: dff['local'].str.upper(),
        local = lambda dff: where(dff['local_upper'].str.strip() == ",", "", dff['local_upper']),
    )
    .query('data > "2022-01-01" and link.str.contains("chronomax")')
    .loc[:, ['prova', 'local', 'data', 'link']]
    .reset_index(drop=True)
)

eventos_chronomax.to_csv('chronomax_runs_tratado.csv', index=False)

