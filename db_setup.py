from db import mydb

#Crear BD
mycursor = mydb.cursor(dictionary=True) #Configurar el cursor para que devuelva diccionarios en lugar de tuplas
mycursor.execute('CREATE DATABASE IF NOT EXISTS crud_compras')

mycursor.execute('USE crud_compras')#Le dice a las tablas en que base de datos se van a crear
mycursor.execute('CREATE TABLE IF NOT EXISTS productos (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(100), bandera VARCHAR(2), precio INT(5), moneda VARCHAR(10))') #AUTO_INCREMENT para ids automáticos
mycursor.execute('CREATE TABLE IF NOT EXISTS carrito '
'                   (id INT, ' \
'                   cantidad INT(5), ' \
'                   FOREIGN KEY (id) REFERENCES productos(id))') 

sql =  'INSERT INTO productos (nombre, bandera, precio, moneda) VALUES (%s, %s,%s, %s)'

val = [
  ('Aleman inicial', 'de', 1500,'€'),
  ('Ruso intermedio', 'ru', 2500,'₽'),
  ('Portugues avanzado', 'br', 3500,'R$'),
  ('Ingles avanzado', 'gb', 2950,'£'),
  ('Chino inicial', 'cn', 6500,'¥'),
  ('Frances avanzado', 'fr', 8600,'€'),
  ('Japones intermedio', 'jp', 1100,'¥'),
  ('Italiano inicial', 'it', 1200,'€'),
  ('Español intermedio', 'es', 9500,'€')
]
#Se vacian las tablas productos y carritos para que cada vez que se ejecute el archivo, no se dupliquen los datos
mycursor.execute('DELETE from carrito')
mycursor.execute('DELETE from productos')
mycursor.execute('ALTER TABLE productos AUTO_INCREMENT = 1')#Resetear Id's
mycursor.executemany(sql, val)
mydb.commit()



