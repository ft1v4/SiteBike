from flask import Flask, redirect, url_for, request, render_template 
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sucesso/<name>')
def sucesso(name):
    return render_template('gg.html', name = name)

@app.route('/compra')
def compra():
    return render_template('compra.html')

@app.route('/erro')
def erro():
    return 'BURRO'

@app.route('/inicio')
def inicio():
    return render_template('login.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
 if request.method == 'POST':
        user = request.form['nome']
        senhaC = request.form['senha']
        if user == '' and senhaC == '':
             return redirect(url_for('erro'))
        else:
            return redirect(url_for('sucesso' , name = user ) )

app.run(debug=True)