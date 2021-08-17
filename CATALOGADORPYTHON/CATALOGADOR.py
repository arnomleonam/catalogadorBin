# Importando a biblioteca MySQL
import pymysql

#Criando a connexão com o servidor

conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'catalogadorbd'
)

cursor = conexao.cursor()
cursor.execute("CREATE TABLE comcliente (nome VARCHAR (255),senha VARCHAR(255))")
