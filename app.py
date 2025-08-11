from flask import Flask, render_template, request

# Inicializa a aplicação Flask
app = Flask(__name__)

# Rota para a página inicial (index.html)
@app.route('/')
def index():
    return render_template('index.html')

# Rota para a página de seleção de orçamento
@app.route('/orcamento.html')
def orcamento():
    return render_template('orcamento.html')

# Rota para o formulário de orçamento
@app.route('/formulario.html')
def formulario():
    # O 'request.args.get' pega o parâmetro 'tipo' da URL (ex: ?tipo=azulejo)
    # e passa-o para o template, mas o seu JavaScript já faz isso, então apenas servimos a página.
    return render_template('formulario.html')

# Rota para o formulário de laudo
@app.route('/laudo.html')
def laudo():
    return render_template('laudo.html')

# Esta parte é opcional, serve para testar localmente antes de enviar para o Render
if __name__ == '__main__':
    app.run(debug=True)