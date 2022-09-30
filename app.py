
#el eje central de la herramienta

from flask import Flask, render_template # aca importamos la libreria

#creamos una varible para ejecutar la app

app = Flask(__name__)#creamos el espacio de tabajo para trabajar conflask
#creamos un entorno para  poder ejecutar y ver si esta funcionando


#creamos funciones--creamos una ruta para poder trabajar
@app.route('/')#definimos la ruta /, la raiz del ducumento
def Index():
   return render_template('Index.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/Login')
def Login():
    return"Este espacio es para un Formulario"







if __name__ =='__main__': #garantizamos que el espacio de trabajo sea el principal
    app.run(port=3000,debug=True) #creamos el puerto y el debug que siempre se vean reflejados los cambios


