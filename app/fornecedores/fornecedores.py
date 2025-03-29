from flask import Blueprint, render_template, redirect, url_for
from app.funcoes import FornecedoresDB
from app.form import RegistrarFornecedores, EditarFornecedor

fornecedores_bp = Blueprint('fornecedores_bp', __name__,
                            template_folder='templates',
                            static_folder='static',
                            static_url_path='/fornecedores/static')


@fornecedores_bp.route('/')
@fornecedores_bp.route('/fornecedores')
def index():
    fornecedores_db = FornecedoresDB().ler()
    return render_template('/fornecedores.html', fornecedores=fornecedores_db)


@fornecedores_bp.route('/excluir_fornecedor/<int:id>')
def excluir_fornecedor(id):
    FornecedoresDB().excluir_fornecedor(id=id)
    return redirect(url_for('fornecedores_bp.index'))


@fornecedores_bp.route('/adicionar_fornecedores', methods=['GET', 'POST'])
def adicionar_fornecedores():
    form = RegistrarFornecedores()

    if form.validate_on_submit():
        FornecedoresDB().inserir(nome_fornecedor=form.fornecedor.data, nome_produto=form.produto.data, preco=form.preco.data.replace(',', '.'), numero_de_contato=form.numero_de_contato.data)
        return redirect('/fornecedores')
    
    return render_template('/adicionar_fornecedores.html', form=form)

    
@fornecedores_bp.route('/editar_fornecedor/<int:id>', methods=['GET', 'POST'])
def editar_fornecedor(id):
    nome_fornecedor = FornecedoresDB().nome_do_fornecedor(id=id)
    form = EditarFornecedor()

    if form.validate_on_submit():
        FornecedoresDB().alterar_dados_fornecedor(id=id ,nome_fornecedor=form.fornecedor.data, nome_produto=form.produto.data, preco=form.preco.data.replace(',', '.'), numero_de_contato=form.numero_de_contato.data)
        return redirect('/fornecedores')
    
    return render_template('/editar_fornecedor.html', nome_fornecedor=nome_fornecedor, form=form)