from flask import Blueprint, url_for, render_template, redirect
from app.funcoes import EstoquesDB, FornecedoresDB
from app.form import RegistrarEstoque, EditarEstoque

estoque_bp = Blueprint('estoque_bp', __name__,
                      template_folder='templates',
                      static_folder='static',
                      static_url_path='/estoque/static')


@estoque_bp.route('/estoques')
def estoque():
    estoques_db = EstoquesDB().ler()
    return render_template('/estoque.html', estoques=estoques_db)


@estoque_bp.route('/adicionar_estoque', methods=['GET', 'POST'])
def adicionar_estoque():
    form = RegistrarEstoque()

    fornecedores_db = FornecedoresDB().ler()
    form.fornecedor.choices = [(fornecedor['nome_fornecedor'], fornecedor['nome_fornecedor']) for fornecedor in fornecedores_db]

    if form.validate_on_submit():
        EstoquesDB().inserir(nome_produto=form.produto.data, nome_fornecedor=form.fornecedor.data, quantidade=form.quantidade.data.replace(',', '.'))
        return redirect(url_for('estoque_bp.estoque'))
    
    return render_template('/adicionar_estoque.html', form=form)


@estoque_bp.route('/excluir_estoque/<int:id>')
def excluir_estoque(id):
    EstoquesDB().excluir_estoque(id=id)
    return redirect(url_for('estoque_bp.estoque'))


@estoque_bp.route('/editar_estoque/<int:id>', methods=['GET', 'POST'])
def editar_estoque(id):
    form = EditarEstoque()

    fornecedores_db = FornecedoresDB().ler()
    form.fornecedor.choices = [(fornecedor['nome_fornecedor'], fornecedor['nome_fornecedor']) for fornecedor in fornecedores_db]

    if form.validate_on_submit():
        EstoquesDB().alterar_dados_estoque(id=id , nome_produto=form.produto.data, nome_fornecedor=form.fornecedor.data, quantidade=form.quantidade.data.replace(',', '.'))
        print('estoque alterado')
        return redirect(url_for('estoque_bp.estoque'))
    
    return render_template('/editar_estoque.html', form=form)