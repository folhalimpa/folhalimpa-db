import csv
from database import Database

class ImportToMysql(object):

    @staticmethod
    def start():

        connection = Database()
        sqlinsert = "INSERT INTO folha_municipal_tce (`cd_ugestora`, `de_ugestora`, `de_cargo`, `de_tipocargo`, `cd_cpf`, `dt_mesanorefencia`, `no_servidor`, `vl_vantagens`, `de_uorcamentaria`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        with open('./data/TCE-PB-SAGRES-Folha_Pessoal_Esfera_Municipal.csv', 'r') as csvfile:
            spamreader = csv.reader(csvfile, delimiter='|')
            next(spamreader)
            count = 0
            for row in spamreader:
                if(len(row) == 9):
                    count = count + 1
                    insertlist = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                    connection.query_insert(sqlinsert, insertlist)

        connection.close_connection()
        print (count)

ImportToMysql.start()
