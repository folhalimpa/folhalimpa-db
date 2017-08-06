from database import Database

class CreateRelationalTablesMunicipios(object):

    @staticmethod
    def addServidores():
        connection = Database()
        sqlSelect = "SELECT DISTINCT cd_cpf FROM folha_municipal_tce"
        selectList = ()
                
        cpfs = connection.query_select(sqlSelect, selectList)

        for cpf in cpfs:
            sqlSelect = "SELECT no_servidor FROM folha_municipal_tce WHERE cd_cpf=%s LIMIT 1"
            selectList = (cpf[0])
            nome = connection.query_select(sqlSelect, selectList)

            sqlinsert = "INSERT INTO servidores_municipios (`nome`, `cpf`) VALUES (%s, %s)"
            insertlist = (nome[0][0], cpf[0])
            connection.query_insert(sqlinsert, insertlist)

        connection.close_connection()

    
    @staticmethod
    def addUnidadesGestoras():
        connection = Database()
        sqlSelect = "SELECT DISTINCT cd_ugestora FROM folha_municipal_tce"
        selectList = ()
                
        cd_ugestoras = connection.query_select(sqlSelect, selectList)

        for cd_gestora in cd_ugestoras:
            sqlSelect = "SELECT de_ugestora FROM folha_municipal_tce WHERE cd_ugestora=%s LIMIT 1"
            selectList = (cd_gestora[0])
            nome = connection.query_select(sqlSelect, selectList)

            sqlinsert = "INSERT INTO unidades_gestoras_municipios (`codigo`, `nome`) VALUES (%s, %s)"
            insertlist = (cd_gestora[0], nome[0][0])
            connection.query_insert(sqlinsert, insertlist)

        connection.close_connection()
    

    @staticmethod
    def addUnidadesOrcamentarias():
        connection = Database()
        sqlSelect = "SELECT DISTINCT de_uorcamentaria FROM folha_municipal_tce"
        selectList = ()
                
        uOrcamentarias = connection.query_select(sqlSelect, selectList)

        for uOrcamentaria in uOrcamentarias:
            sqlinsert = "INSERT INTO unidades_orcamentarias_municipios (`nome`) VALUES (%s)"
            insertlist = (uOrcamentaria[0])
            connection.query_insert(sqlinsert, insertlist)

        connection.close_connection()
    

    @staticmethod
    def addCargos():
        connection = Database()
        sqlSelect = "SELECT DISTINCT de_cargo FROM folha_municipal_tce"
        selectList = ()
                
        cargos = connection.query_select(sqlSelect, selectList)

        for cargo in cargos:
            sqlinsert = "INSERT INTO cargos_municipios (`nome`) VALUES (%s)"
            insertlist = (cargo[0])
            connection.query_insert(sqlinsert, insertlist)

        connection.close_connection()
        

    @staticmethod
    def addTiposDeCargos():
        connection = Database()
        sqlSelect = "SELECT DISTINCT de_tipocargo FROM folha_municipal_tce"
        selectList = ()
                
        tiposDeCargos = connection.query_select(sqlSelect, selectList)

        for tipoDeCargo in tiposDeCargos:
            sqlinsert = "INSERT INTO vinculos_municipios (`nome`) VALUES (%s)"
            insertlist = (tipoDeCargo[0])
            connection.query_insert(sqlinsert, insertlist)

        connection.close_connection()

    @staticmethod
    def start():
        print('Realizando addServidores() ...')
        CreateRelationalTablesMunicipios.addServidores()

        print('Realizando addUnidadesGestoras() ...')
        CreateRelationalTablesMunicipios.addUnidadesGestoras()

        print('Realizando addUnidadesOrcamentarias() ...')
        CreateRelationalTablesMunicipios.addUnidadesOrcamentarias()

        print('Realizando addCargos() ...')
        CreateRelationalTablesMunicipios.addCargos()

        print('Realizando addTiposDeCargos() ...')
        CreateRelationalTablesMunicipios.addTiposDeCargos()



CreateRelationalTablesMunicipios.start()
