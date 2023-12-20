# web-scraping-run-results
Repositório com  scripts para extrair resultados de corrida

# Scraping com scrapy

Em alguns sites, extrair dados pode se tornar um desafio quando as informações não estão disponíveis diretamente no HTML. Isso acontece quando as visualizações e dados são expostos dinamicamente, de acordo com as interações do usuário. Os dados podem ser gerados através de scripts ou por APIs. Aqui vou falar um pouco de como extrair dados de sites que geram dados por APIs.

Para extrair os dados de sites que usam uma api para gerar os resultados dinamicamente, a melhor forma que conheço até o momento é através da ferramenta `scrapy`, do python.

Primeiro, para utilizá-la, instale a biblioteca scrapy no seu ambiente:

```bash
pip install scrapy
```

Em seguida, vamos criar um projeto com scrapy. Com o terminal na pasta que vc vai criar os projetos, digite o seguinte comando:
```bash
scrapy startproject <nome-do-seu-projeto>
```

Substitua \<nome-do-seu-projeto\> pelo nome que você quer utilizar. No meu caso ficou assim:

```bash
scrapy startproject resultados_ativo
```

Dentro da sua pasta de trabalho deve aparecer a seguinte estrutura de pasta:
```
├── <nome-do-seu-projeto>
│   ├── <nome-do-seu-projeto>
│   │   ├── spiders
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   ├── items.py
│   │   ├── middlewares.py
│   │   ├── pipelines.py
│   │   └── settings.py
│   └── scrapy.cfg
```

A partir de agora vou usar o nome do meu projeto nos exemplos. Seguindo para o próximo passo, de volta ao terminal navegue para a pasta do seu projeto:
```bash
cd .\resultados_ativo\ 
```
Para extrair os dados com scrapy, é criado um spider que configuraremos com python. Para criar esse spider, digite o seguinte comando no terminal `scrapy genspider <nome-do -spider> <site-que-contem-os-dados>`. O site que contém os dados que quero extrair está nesse [link](https://www.ativo.com/calendario/eventos/america-do-sul/br/mg/belo-horizonte/corrida-de-rua/38542/circuito-das-estacoes-2023-primavera-belo-horizonte/), mas não precisa se preocupar tanto com o link nesse momento. Tanto que no meu caso vou colocar somente o site raiz por enquanto. Nos próximos passos vou inspecionar o site pra pegar o link da api usado pra fazer requests e trocá-lo no script. Por enquanto, no meu caso, ficou assim:
```bash
scrapy genspider ativo https://www.ativo.com/
```

Na sua estrutura de pastas, dentro da pasta `spiders` deve aparecer um script com o nome do seu spider. Como eu nomeei meu spider como `ativo`, minha estrutura fica assim:

```
├── <nome-do-seu-projeto>
│   ├── <nome-do-seu-projeto>
│   │   ├── spiders
│   │   │   ├── ativo.py
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   ├── items.py
│   │   ├── middlewares.py
│   │   ├── pipelines.py
│   │   └── settings.py
│   └── scrapy.cfg
```
## Chronomax
Um dos sites que compilam resultados de grandes corridas, a Chronomax, apresenta os dados bem estruturados. No entanto, a extração dos dados através do scrapy, por algum motivo, não funciona como esperado.

Foram feitas algumas tentativas com a dupla splash + scrapy, mas também sem sucesso. Dessa forma, por enquanto, a extração será feita com selenium. A extração com selenium é mais lenta, mas consegue extrair os dados da Chronomax.

