from flask import Flask, render_template,request, url_for, redirect, abort,render_template
app= Flask(__name__)#NAME se refiere a main 
#-----------------------------------
#Base de datos
import mysql.connector#Importamos la base de datos

midb=mysql.connector.connect(#Aqui hacemos la conexion con la base de datos
     host="localhost",
     user="root",
     password="cristian1234",
     database="prueba"
)
cursor= midb.cursor(dictionary=True)#Con cursor podemos usar variables que puedan mostrarnos las tablas con los nombres que 
#tenemos referidos a ellos como username etc..

@app.route('/')#Aqui le damos una ruta para cuando ingresamos a http://127.0.0.1:5000
def index():
     return 'Hola mundo'
#-----------------------------------------------------
# @app.route('/post/<post_id>')
# def lala(post_id):
#     return  'El id del pos es: '+ post_id#Esto es para saber que atrabes de la url podemos pasarle inforamcion a python

# @app.route('/lele')
# def lele():
#     return 'lele'

#------------------------------------------------------
# #Aqui usaremos el GET,POST,PUT Y DELETE
# @app.route('/post/<post_id>', methods= ['GET', 'POST'])
# def lili(post_id):
#     if request.method== 'GET':
#         return 'El id del post es :' + post_id
#     else:
#         return 'Este es otro metodo y no GET'

# @app.route('/lele', methods=['POST'])
# def lele():
#     print(request.form)
#     print(request.form['llave1'])
#     print(request.form['llave2'])
#     return 'lele'
#------------------------------------------------------------
#Construccion de urls
# @app.route('/post/<post_id>', methods= ['GET', 'POST'])
# def lala(post_id):
#     if request.method== 'GET':
#         return 'El id del post es :' + post_id
#     else:
#         return 'Este es otro metodo y no GET'

# @app.route('/lele', methods=['POST'])
# def lele():
#     print(url_for('lala', post_id=2))
#     print(request.form)
#     print(request.form['llave1'])
#     print(request.form['llave2'])
#     return 'lele'
#------------------------------------------------------
#Redireccionar al usuario
# @app.route('/post/<post_id>', methods= ['GET', 'POST'])
# def lala(post_id):
#     if request.method== 'GET':
#         return 'El id del post es :' + post_id
#     else:
#         return 'Este es otro metodo y no GET'

# @app.route('/lele', methods=['POST', 'GET'])
# def lele():
#     return redirect(url_for('lala', post_id=2))#Para redireccionar al usuario tenemos que importar REDIRECT el print lo eliminamos 
#     y colocamos redirect y siempre pero siempre tenemos que poner un RETURN
#     return 'lele'
#------------------------------------------------------
#Abortando peticiones
# @app.route('/post/<post_id>', methods= ['GET', 'POST'])
# def lala(post_id):
#     if request.method== 'GET':
#         return 'El id del post es :' + post_id
#     else:
#         return 'Este es otro metodo y no GET'

# @app.route('/lele', methods=['POST', 'GET'])
# def lele():
#     abort(404)#Aqui podemos poner el error para que le muestre al usuario 
#     #Lo que tenemos que agregar es importar ABORT y despues le colocamos abort(404) que seria el mas comun
#     return redirect(url_for('lala', post_id=2))
#     return 'lele' 
#---------------------------------------------------------------
#Rederizando plantillas
# @app.route('/post/<post_id>', methods= ['GET', 'POST'])
# def lala(post_id):
#     if request.method== 'GET':
#         return 'El id del post es :' + post_id
#     else:
#         return 'Este es otro metodo y no GET'

# @app.route('/lele', methods=['POST', 'GET'])
# def lele():
#     return render_template('lele.html')#Primero tenemos que exportar RENDER_TEMPLATE lo que hacemos con esto
#     #es enviarlo a una pagina HTML que creamos en TEMPLATES y le colocamos el nombre del archivo html.
#---------------------------------------------------
#Respondiendo con JSON
# @app.route('/post/<post_id>', methods= ['GET', 'POST'])
# def lala(post_id):
#     if request.method== 'GET':
#         return 'El id del post es :' + post_id
#     else:
#         return 'Este es otro metodo y no GET'

# @app.route('/lele', methods=['POST', 'GET'])
# def lele():
#     return {#Este es en modo JSON se hace con un diccionario y sirve bastante con las APIS
#         "userman": "Quiroz",
#         "Email": "Quiroz@gmail.com"
#     }
#------------------------------------------
#Extendiendo Plantillas
# @app.route('/home1', methods=['GET'])
# def home():
#     return render_template('home.html', mensaje='Hola mundo')
#------------------------------------------
#Mostrando la  base de datos
@app.route('/lele', methods=['POST', 'GET'])
def lele():
    cursor.execute('select * from Usuario')#Aqui seleccionamos tabla de Usuario con lo demas que tiene
    usuarios = cursor.fetchall()#Guardamos en una variable todo los datos de la tabla
    print(usuarios)#Aqui lo imprimimos en nuestra plantilla
    return render_template('lele.html', usuarios=usuarios)#Aqui usamos el archivo html y guardamos la variable de usuarios en usuarios
#--------------------------------------------------
#Ingresando registros en base de datos
@app.route('/crear', methods=['GET', 'POST'])
def crear():
     if request.method== "POST":
          username= request.form['username']
          email = request.form['email']
          edad = request.form['edad']
          sql = "insert into Usuario (username , email, edad) values (%s, %s, %s)"
          values= (username, email, edad)
          cursor.execute(sql,values)
          midb.commit()

          return redirect(url_for('lele'))
     return render_template('crear.html' )