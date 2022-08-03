import mysql.connector#Para poder ingresar a la base de datos de mysql tenemos que importalo primero

midb=mysql.connector.connect(#Tenemos que hacer una variable para que podamos usar la base de datos
    host='localhost',
    user='root',#Estos son los parametros de la base de datos y que tabla estamos usando
    password='cristian1234',
    database='prueba'
)

cursor=midb.cursor()#Gracias a que tenemos una variable donde se guarda la base de datos tenemos que usar cursor para poder ejecutar funciones

cursor.execute('select * from Usuario') #Aqui el ejemplo para poder ejecutar la base de datos y el comando que estamos usando son de sql

resultado=cursor.fetchall()#Nosotros en la base de datos pedimos todos los datos por eso esta FETCHALL para tomar todos los datos 
#pero si silamente queremos 1 tenemos que usar FETCHONE y lo guardamos el resultado en una variable
print(resultado)#Aqui podemos mostrar los datos que tenga la base de datos