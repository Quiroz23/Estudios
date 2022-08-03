import mysql.connector

midb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='cristian1234',
    database='prueba'
)
cursor=midb.cursor()

# Listar datos
#cursor.execute ('select * from usuario')
# resultado =cursor.fetchall
# print(resultado)

#insertar datos
#En values tenemos que si o si poner todos los datos que tenemos en nuestra tabla
# sql= ('insert into usuario ('email,username , edad') values (%s,%s,%s)
# values= ('correo@gmail.com', 'Usuario' , 25)#Aqui podemos ingresar los datos 

# cursor.execute(sql,values)#Aqui ejecutamos para que ingrese los datos

#Actualizar datos
# sql= 'update usuario set email= %s where id = %s'#Aqui podemos actualizar los datos que queremos en la base de datos 
#por que ponemos %S es porque le damos los valores que queremos actualizar en values
# values =('juan@gmail.com', 4)
# midb.commit()
#print(cursor.rowcount)

# # Eliminar datos
# sql= 'delete from usuarios where id= %s'#Aqui podemos eliminar los datos de una tabla como queramos en este ejemplo quisimos 
# #Eliminarlo con el id
# values = (4, )#Aqui ponemos el id que queremos eliminar y siempre tendremos que usar una COMA
# cursor.execute(sql, values)#Aqui ejecutamos las funciones que queremos que ejecute PYTHON en la base de datos
# midb.commit()

# Limitar los resultados

cursor.execute('select * from usuario limit 1')#Aqui limitamos los datos a que nos muestre solamente 1 dato al igual podemos hacer que nos muestre dos datos al poner 2
resultado= cursor.fetchall()
print(resultado)