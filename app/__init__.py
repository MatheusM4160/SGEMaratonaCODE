from flask import Flask
from app.config import Config

from app.fornecedores.fornecedores import fornecedores_bp
from app.estoque.estoque import estoque_bp

app = Flask(__name__)

app.register_blueprint(fornecedores_bp)
app.register_blueprint(estoque_bp)

app.config.from_object(Config)
