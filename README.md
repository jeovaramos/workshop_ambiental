# Me formei e agora?
## Ciência de dados ambientais


O dashboard (`app.py`) é o produto de dados, resultado dessa análise. Nele estou trazendo somente a visualização dos principais resultados.

Não deixe de conferir o [relatório de resultados](https://docs.google.com/document/d/1yYwSWtm4WC0OuR-4VREUkzJp3iORV3rBGOyZmN1H_-8/edit?usp=sharing) para conferir as motivações e discussões dos mesmos. Confira também o [relatório de atividades](https://docs.google.com/document/d/1-fdSSZdLONQsEqbWauxyfFhzOCtKa0i2Ru-Gi43Pzzc/edit?usp=sharing).

Aproveite para explorar também os commits e os PR deste repositório para verificar o cumprimento do planejamento durante o desenvolvimento do projeto.

# Preparação do ambiente:
1. Clone o repositório

`git clone https://github.com/jeovaramos/world_happiness.git`

2. Crie um ambiente virtual dentro do repositório baixado

`python3 -m venv .venv`
`source .venv/bin/activate`

3. Instale as dependencias no ambiente virtual

`pip install -r requirements/dev.txt`

Se estiver tendo problemas para instalar a biblioteca pymc2, considere instalar a dependência NetCDF-4 manualmente: [link]("https://docs.geoserver.org/stable/en/user/extensions/netcdf-out/nc4.html")

# Análise dos resultados
4. Para rodar localmente o dashboard use o comando:
`streamlit run app.py`

5. No Notebook disponível na branch analytics, certifique-se de usar o kernel correto. Você pode abri-lo na sua IDE preferida.
