from app import app
from flask import render_template, redirect ,url_for, flash
from app.form import RegistrarFornecedores, EditarFornecedor

from app.funcoes import FornecedoresDB, EstoquesDB

@app.route('/')
@app.route('/fornecedores')
def index():
    fornecedores_db = FornecedoresDB().ler()
    return render_template('fornecedores/fornecedores.html', fornecedores=fornecedores_db)

@app.route('/excluir_fornecedor/<int:id>')
def excluir_fornecedor(id):
    FornecedoresDB().excluir_fornecedor(id=id)
    return redirect(url_for('index'))

@app.route('/adicionar_fornecedores', methods=['GET', 'POST'])
def adicionar_fornecedores():
    form = RegistrarFornecedores()
    if form.validate_on_submit():
        FornecedoresDB().inserir(nome_fornecedor=form.fornecedor.data, nome_produto=form.produto.data, preco=form.preco.data.replace(',', '.'), numero_de_contato=form.numero_de_contato.data)
        return redirect('/fornecedores')
    return render_template('fornecedores/adicionar_fornecedores.html', form=form)
    
@app.route('/editar_fornecedor/<int:id>', methods=['GET', 'POST'])
def editar_fornecedor(id):
    nome_fornecedor = FornecedoresDB().nome_do_fornecedor(id=id)
    form = EditarFornecedor()
    if form.validate_on_submit():
        FornecedoresDB().alterar_dados_fornecedor(id=id ,nome_fornecedor=form.fornecedor.data, nome_produto=form.produto.data, preco=form.preco.data.replace(',', '.'), numero_de_contato=form.numero_de_contato.data)
        return redirect('/fornecedores')
    return render_template('fornecedores/editar_fornecedor.html', nome_fornecedor=nome_fornecedor, form=form)

@app.route('/estoques')
def estoque():
    estoques_db = EstoquesDB().ler()
    return render_template('estoques/estoque.html', estoques=estoques_db)

@app.route('/perfil')
def perfil():
    return render_template('perfil/perfil.html')