from flask import Flask
from flask import render_template, request, redirect, url_for, flash
from cod_decod_morse import codificar_mensaje as cm, codificar_palabra as cp, decodificar_mensaje as dm, decodificar_palabra as dp 
import re

app = Flask(__name__)
app.secret_key ="WilmerPerdomo"

@app.route('/')
def index():

    return render_template('morse/index.html')

@app.route('/cod_decod', methods=['POST', 'GET'])
def cod_decod():

    mensaje = request.form['mensaje']
    opcion = request.form['opcion']

    if mensaje =='' or opcion =='':
        flash('Recuerda llenar los datos de los campos')
        return redirect(url_for('index'))

    if opcion == 'CODIFICAR':
        for m in mensaje:
            if re.search(m,'.') or re.search(m,'-'):
                flash('Seleccione la opcion correcta')
                return redirect(url_for('index'))  

        resultado = cm(mensaje)

    if opcion == 'DECODIFICAR':
        print(mensaje)
        for m in mensaje:
            if re.search(m,'.') or re.search(m,'-'):
                resultado =dm(mensaje)
                break
            else:
                flash('Seleccione la opcion correcta')
                return redirect(url_for('index')) 
        
                        
    return render_template('morse/resultado.html', resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)