from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired

class RegistrarFornecedores(FlaskForm):
    fornecedor = StringField('Fornecedor', validators=[DataRequired()])
    produto = StringField('Produto', validators=[DataRequired()])
    numero_de_contato = StringField('Número de Contato', validators=[DataRequired()])
    botao_cadastrar = SubmitField('Cadastrar')