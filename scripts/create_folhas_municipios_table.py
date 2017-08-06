from database import Database

class CreateFolhasMunicipiosTable(object):

    @staticmethod
    def start():

        print("Populando Tabela folhas_municipios...")

        connection = Database()
        sqlSelect = "SELECT * FROM folha_municipal_tce"
        selectList = ()

        rows = connection.query_select(sqlSelect, selectList)

        for row in rows:
            cd_ugestora = row[1]
            de_ugestora = row[2]
            de_cargo = row[3]
            de_tipocargo = row[4]
            cd_cpf = row[5]
            dt_mesanoreferencia = row[6]
            no_servidor = row[7]
            vl_vantagens = row[8]
            de_uorcamentaria = row[9]

            # Pega o ID que será a chave estrangeira para identificar essa unidade gestora
            sqlSelect = "SELECT id FROM unidades_gestoras_municipios WHERE codigo=%s LIMIT 1"
            selectList = (cd_ugestora)
            result_query = connection.query_select(sqlSelect, selectList)
            id_unidade_gestora = result_query[0][0]

            # Pega o ID que será a chave estrangeira para identificar essa cargo
            sqlSelect = "SELECT id FROM cargos_municipios WHERE nome=%s LIMIT 1"
            selectList = (de_cargo)
            result_query = connection.query_select(sqlSelect, selectList)
            id_cargo = result_query[0][0]

            # Pega o ID que será a chave estrangeira para identificar esse tipo do vinculo
            sqlSelect = "SELECT id FROM vinculos_municipios WHERE nome=%s LIMIT 1"
            selectList = (de_tipocargo)
            result_query = connection.query_select(sqlSelect, selectList)
            id_vinculo = result_query[0][0]

            # Pega o ID que será a chave estrangeira para identificar esse servidor
            sqlSelect = "SELECT id FROM servidores_municipios WHERE cpf=%s LIMIT 1"
            selectList = (cd_cpf)
            result_query = connection.query_select(sqlSelect, selectList)
            id_servidor = result_query[0][0]

            # Pega o ID que será a chave estrangeira para identificar essa unidade orçamentária
            sqlSelect = "SELECT id FROM unidades_orcamentarias_municipios WHERE nome=%s LIMIT 1"
            selectList = (de_uorcamentaria)
            result_query = connection.query_select(sqlSelect, selectList)
            id_unidade_orcamentaria = result_query[0][0]

            # Monta string para query de insert onde o campo data_pagamento é do tipo DATE
            data_pagamento = dt_mesanoreferencia[2:] + "-" + dt_mesanoreferencia[:2] + "-1"
            # Converte o string de valor para float com apenas duas casas decimais
            valor = round(float(vl_vantagens), 2)

            # Uma vez que já temos todos os IDs que serão chaves estrangeiras da nova tabela de pagementos
            # relacional, podemos então adicionar esse registro na tabela folhas_municipios
            sqlinsert = "INSERT INTO folhas_municipios (`id_servidor`, `id_cargo`, `id_vinculo`, `id_unidade_gestora`, `id_unidade_orcamentaria`, `data_pagamento`, `valor`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            insertlist = (id_servidor, id_cargo, id_vinculo, id_unidade_gestora, id_unidade_orcamentaria, data_pagamento, valor)
            connection.query_insert(sqlinsert, insertlist)


        connection.close_connection()


CreateFolhasMunicipiosTable.start()
