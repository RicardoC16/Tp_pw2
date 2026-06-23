#Creo la conexion a la base
import mysql.connector

mydb = mysql.connector.connect(
  host='localhost',
  port= 3306,
  user='root',
  password='root',
  database='crud_compras'
)