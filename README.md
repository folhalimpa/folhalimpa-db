# Folha Limpa DB

Folha Limpa é um projeto do Hackfest 2017 que tem como objetivo exibir visualizações de anomalias nas folhas de pagamento do estado e dos municípios da Paraíba.

O Folha Limpa pode ser acessado no endereço: [folhalimpa.org](http://folhalimpa.org/).

## Como executar localmente

O Folha Limpa utiliza o [Docker](https://www.docker.com) para sua execução.

Para construir a imagem do docker do banco de dados, execute de dentro da raiz do projeto:

`docker-compose build`

O docker construirá uma imagem a partir do `Dockerfile` e depois que o processo terminar você verá uma imagem chamada `fl-db` quando executar o comando `docker images`.

## Importando dados

O banco de dados MySQL é criado a partir dos [dados de folhas de pagamento]("https://dados.tce.pb.gov.br/TCE-PB-SAGRES-Folha_Pessoal_Esfera_Municipal.txt.gz") dos municípios da Paraíba disponibilizados pelo TCE.
Com esse arquivo em mãos, execute os scripts encontrados no diretório `scripts/mysql` na seguinte ordem:
`import_csv_to_mysql.py`, `create_relational_tables_municipios.py`, `create_folhas_municipios_table.py`.
O arquivo `database.xml` traz algumas configurações do banco de dados utilizado.

No Neo4J, além dos dados das folhas de pagamento dos municípios também é utilizado os [dados estaduais](https://dados.tce.pb.gov.br/TCE-PB-SAGRES-Folha_Pessoal_Esfera_Estadual.txt.gz).
Para isso, execute o código R encontrado em `scripts/neo4j` para gerar o arquivo `dadosAcumulados.csv`.
Esse arquivo é utilizado pelo `cypher`, que deve ser executado dentro do Neo4J para criar o grafo.

