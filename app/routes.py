from app import app
from flask import render_template, redirect ,url_for, flash
from app.form import RegistrarFornecedores

from app.funcoes import FornecedoresDB

@app.route('/')
@app.route('/fornecedores')
def index():
    fornecedores_db = FornecedoresDB().ler()
    return render_template('fornecedores.html', fornecedores=fornecedores_db)

@app.route('/excluir_fornecedor/<int:id>')
def excluir_fornecedor(id):
    FornecedoresDB().excluir_fornecedor(id=id)
    return redirect(url_for('index'))

@app.route('/adicionar_fornecedores', methods=['GET', 'POST'])
def adicionar_fornecedores():
    form = RegistrarFornecedores()
    if form.validate_on_submit():
        FornecedoresDB().inserir(nome_fornecedor=form.fornecedor.data, nome_produto=form.produto.data, numero_de_contato=form.numero_de_contato.data)
        return redirect('/fornecedores')
    return render_template('adicionar_fornecedores.html', form=form)
    
@app.route('/editar_fornecedor')
def editar_fornecedor():
    return render_template('editar_fornecedor.html')

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')