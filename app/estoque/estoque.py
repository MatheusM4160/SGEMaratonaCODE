from flask import Blueprint, url_for, render_template, redirect
from app.funcoes import EstoquesDB

estoque_bp = Blueprint('estoque_bp', __name__,
                      template_folder='templates',
                      static_folder='static',
                      static_url_path='/estoque/static')

@estoque_bp.route('/estoques')
def estoque():
    estoques_db = EstoquesDB().ler()
    return render_template('/estoque.html', estoques=estoques_db)