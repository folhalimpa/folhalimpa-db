# Folha Limpa DB

Folha Limpa é um projeto do Hackfest 2017 que tem como objetivo exibir visualizações de anomalias nas folhas de pagamento do estado e dos municípios da Paraíba.

O Folha Limpa pode ser acessado no endereço: [folhalimpa.org](http://folhalimpa.org/).

## Como executar localmente

Pra construir a imagem do docker, de dentro da raiz do projeto execute:

`docker-compose build`

O docker vai construir uma imagem a partir do `Dockerfile` e depois que o processo terminar você vai ver uma imagem chamada `fl-db` quando executar o comando `docker images`.
