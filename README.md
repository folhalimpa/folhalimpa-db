# Folha Limpa DB

Folha Limpa é um projeto do Hackfest 2017 que tem como objetivo exibir visualizações de anomalias nas folhas de pagamento do estado e dos municípios da Paraíba.

O Folha Limpa pode ser acessado no endereço: [folhalimpa.org](http://folhalimpa.org/).

## Como executar localmente

O Folha Limpa utiliza o [Docker](https://www.docker.com) para sua execução.

Para construir a imagem do docker do banco de dados, execute de dentro da raiz do projeto:

`docker-compose build`

O docker construirá uma imagem a partir do `Dockerfile` e depois que o processo terminar você verá uma imagem chamada `fl-db` quando executar o comando `docker images`.
