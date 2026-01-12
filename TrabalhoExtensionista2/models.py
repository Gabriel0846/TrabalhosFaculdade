from datetime import datetime
from database import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class PontoColeta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(200), nullable=False)
    tipos_descarte = db.Column(db.Text, nullable=False)  # JSON string de tipos
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    telefone = db.Column(db.String(20))
    horario_funcionamento = db.Column(db.String(100))
    observacoes = db.Column(db.Text)
    data_cadastro = db.Column(db.DateTime, default=datetime.utcnow)
    ativo = db.Column(db.Boolean, default=True)
    oculto = db.Column(db.Boolean, default=False)  # Novo campo
    
    feedbacks = db.relationship('Feedback', backref='ponto_coleta', lazy=True)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ponto_coleta_id = db.Column(db.Integer, db.ForeignKey('ponto_coleta.id'))
    avaliacao = db.Column(db.Integer)
    comentario = db.Column(db.Text)
    tipo_feedback = db.Column(db.String(50))
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    contato = db.Column(db.String(100))
    lido = db.Column(db.Boolean, default=False)
    salvo = db.Column(db.Boolean, default=False)
    respondido = db.Column(db.Boolean, default=False)
    resposta = db.Column(db.Text)
    data_resposta = db.Column(db.DateTime)
    
    # Método para marcar como lido
    def marcar_como_lido(self):
        self.lido = True
        db.session.commit()