
#el eje central de la herramienta


from flask import Flask, render_template, request # aca importamos la libreria
#conexion a la base de datos
from flask_mysqldb import MySQL ##primero importamos

#creamos una varible para ejecutar la app

app = Flask(__name__)#creamos el espacio de tabajo para trabajar conflask
#creamos un entorno para  poder ejecutar y ver si esta funcionando

#configuracion de la conexion de la base de datos
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_BD']='proyecto'
mysql=MySQL(app)


#creamos funciones--creamos una ruta para poder trabajar
@app.route('/')#definimos la ruta /, la raiz del ducumento
def Index():
   return render_template('Index.html') 

#crear funcion para almacenar   ..definimos la ruta

@app.route('/AddUsuario', methods=['POST'])#a donde se dirije y a donde va a recibir los datoss SIEMPRE EN PLURAL Y EL METODO EN MAYUSCULA
def AddUsuario(): #necesioto que reciba los datos
   if request.method=='POST':#si la peticion que hago es realizada atravez del metodo post
        Nombre=request.form['Nombre'] #QUE ME TRAIGA LOS DATOS QUE INGRESE ATRAVEZ DEL FORMULARIO
        Edad=request.form['Edad']
        Fecha=request.form['Fecha']
        Email=request.form['Email']
        print(Nombre)
        print(Edad)
        print(Fecha)
        print(Email) 
        #CONEXION A LA BASE DE DATOS
        cur=mysql.connection.cursor()
        cur.execute ('INSERT INTO usuarios(nombres, edad, fechas,email) VALUES (%s,%s,%s,%s)',(Nombre,Edad,Fecha,Email))    
        mysql.connection.commit()
        
        return 'Informacion Recibida'









if __name__ =='__main__': #garantizamos que el espacio de trabajo sea el principal
    app.run(port=3000,debug=True) #creamos el puerto y el debug que siempre se vean reflejados los cambios


