import mysql.connector

midb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='cristian1234',
    database='prueba'
)
cursor=midb.cursor()

#Listar datos
cursor.execute ('select * from usuario')
resultado =cursor.fetchall
print(resultado)

#insertar datos
#En values tenemos que si o si poner todos los datos que tenemos en nuestra tabla
sql= 'insert into Usuario("email,username , edad") values(%s,%s,%s)'
values= ('correo@gmail.com', 'Usuario' , 25)#Aqui podemos ingresar los datos 

cursor.execute(sql,values)#Aqui ejecutamos para que ingrese los datos
midb.commit()

print(cursor.rowcount)