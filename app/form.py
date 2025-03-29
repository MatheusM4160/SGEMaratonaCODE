from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField
from wtforms.validators import DataRequired

class RegistrarFornecedores(FlaskForm):
    fornecedor = StringField('Fornecedor', validators=[DataRequired()])
    produto = StringField('Produto', validators=[DataRequired()])
    preco = StringField('Preço', validators=[DataRequired()])
    numero_de_contato = StringField('Número de Contato', validators=[DataRequired()])
    botao_cadastrar = SubmitField('Cadastrar')

class EditarFornecedor(FlaskForm):
    fornecedor = StringField('Fornecedor')
    produto = StringField('Produto')
    preco = StringField('Preço')
    numero_de_contato = StringField('Número de Contato')
    botao_alterar = SubmitField('Alterar')

class RegistrarEstoque(FlaskForm):
    produto = StringField('Produto', validators=[DataRequired()])
    fornecedor = SelectField('Fornecedor', validators=[DataRequired()])
    quantidade = StringField('Quantidade', validators=[DataRequired()])
    botao_cadastrar = SubmitField('Cadastrar')

class EditarEstoque(FlaskForm):
    produto = StringField('Produto')
    fornecedor = SelectField('Fornecedor')
    quantidade = StringField('Quantidade')
    botao_alterar = SubmitField('Alterar')