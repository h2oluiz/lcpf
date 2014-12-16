#from os import getenv
import pymssql

''''
server = getenv("sbsb21") # Banco Sipra
user = getenv("userasp")
password = getenv("")

conn = pymssql.connect(server, user, password, "SIPRA")
cursor = conn.cursor()


cursor.execute('select_candidato_sp null, '44259069691'')

for row in cursor:
        print('row = %r' % (row,))

        conn.close()
'''

class BuscaSipra:

    def __init__(self):
        self.cpf = None
        self.conn = None

    def conectar(self, consultar):

        server = 'sbsb21' # Banco Sipra
        user = 'userasp'
        password = ''

        conn = pymssql.connect(server, user, password, 'sipra')
        cursor = conn.cursor()
        cursor.execute(consultar)

        if cursor.rowcount == 0:
            return False
        else:
            return True


        conn.close()


    def desconectar(self):
        self.conn.close()

    def busca_cpf(self, cpf):

        if self.conectar("select_candidato_sp null, '%s'" % cpf):
            print "e candidato"
            return True
        elif self.conectar("select * from sipra..log_gerenciamento lg where log_tra_codigo = 4 \n\
                              and replace(replace(log_codigo_atingido,'.',''),'-','') = '%s'" % cpf):
            print "ja foi candidato"
            return True
        elif self.conectar("""SELECT DISTINCT
                                 ROW_NUMBER() OVER(ORDER BY ass.beneficiario_identificacao_codigo ASC) AS RowNumber,
                                 ass.beneficiario_identificacao_codigo,
                                 ass.beneficiario_tiposituacao_codigo,
                                 ass.beneficiario_assentamento_situacao_data
                              --INTO #ben_todas_situacoes
                              FROM beneficiario..beneficiario_assentamento ass
                              INNER JOIN global..sr sr
                                ON sr.sr_super = left(ass.beneficiario_identificacao_codigo,2)
                              inner join beneficiario..beneficiario_identificacao b
                                on ass.beneficiario_identificacao_codigo=b.beneficiario_identificacao_codigo

                              where ass.beneficiario_identificacao_codigo NOT IN
                                     (SELECT beneficiario_identificacao_codigo
                                       FROM beneficiario..beneficiario_assentamento
                                       WHERE beneficiario_tiposituacao_codigo NOT IN (2, 8, 9, 12, 13, 15, 16))
                              and b.beneficiario_identificacao_cpf = '%s'

                              order by ass.beneficiario_identificacao_codigo, ass.beneficiario_assentamento_situacao_data""" % cpf):
            print "Ja foi beneficiario"
            return True

        else:
            return False




#if __name__ == "__main__":
#    b = BuscaSipra()
#    print b.busca_cpf('26983001672')
