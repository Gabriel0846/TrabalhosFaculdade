from datetime import datetime, timezone
from database import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

def utc_now():
    return datetime.now(timezone.utc)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=utc_now)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class PontoColeta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(200), nullable=False)
    tipos_descarte = db.Column(db.Text, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    telefone = db.Column(db.String(20))
    horario_funcionamento = db.Column(db.String(100))
    observacoes = db.Column(db.Text)
    data_cadastro = db.Column(db.DateTime, default=utc_now)
    ativo = db.Column(db.Boolean, default=True)
    oculto = db.Column(db.Boolean, default=False)
    
    feedbacks = db.relationship('Feedback', backref='ponto_coleta', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self):
        import json
        try:
            tipos = json.loads(self.tipos_descarte) if self.tipos_descarte else []
        except (json.JSONDecodeError, TypeError):
            tipos = [self.tipos_descarte] if self.tipos_descarte else []
        return {
            'id': self.id, 'nome': self.nome, 'endereco': self.endereco,
            'tipos_descarte': tipos, 'latitude': self.latitude, 'longitude': self.longitude,
            'telefone': self.telefone, 'horario_funcionamento': self.horario_funcionamento,
            'observacoes': self.observacoes, 'ativo': self.ativo, 'oculto': self.oculto,
            'data_cadastro': self.data_cadastro.isoformat() if self.data_cadastro else None
        }

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ponto_coleta_id = db.Column(db.Integer, db.ForeignKey('ponto_coleta.id'))
    avaliacao = db.Column(db.Integer)
    comentario = db.Column(db.Text)
    tipo_feedback = db.Column(db.String(50))
    data_criacao = db.Column(db.DateTime, default=utc_now)
    contato = db.Column(db.String(100))
    lido = db.Column(db.Boolean, default=False)
    salvo = db.Column(db.Boolean, default=False)
    respondido = db.Column(db.Boolean, default=False)
    resposta = db.Column(db.Text)
    data_resposta = db.Column(db.DateTime)
    
    def to_dict(self):
        return {
            'id': self.id, 'ponto_coleta_id': self.ponto_coleta_id,
            'ponto_nome': self.ponto_coleta.nome if self.ponto_coleta else 'Não especificado',
            'avaliacao': self.avaliacao, 'comentario': self.comentario,
            'tipo_feedback': self.tipo_feedback, 'contato': self.contato,
            'data_criacao': self.data_criacao.isoformat() if self.data_criacao else None,
            'lido': self.lido, 'salvo': self.salvo, 'respondido': self.respondido,
            'resposta': self.resposta, 'data_resposta': self.data_resposta.isoformat() if self.data_resposta else None
        }