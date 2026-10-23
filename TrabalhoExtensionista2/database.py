from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'admin_login'

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///descarte.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'sua-chave-secreta-aqui'  # Altere para uma chave segura
    
    db.init_app(app)
    login_manager.init_app(app)
    
    with app.app_context():
        db.create_all()
        print("Banco de dados inicializado!")
        
        # Criar usuário admin se não existir
        from models import User
        if not User.query.filter_by(username='admin').first():
            admin_user = User(username='admin', is_admin=True)
            admin_user.set_password('admin123')  # Senha inicial
            db.session.add(admin_user)
            db.session.commit()
            print("Usuário admin criado: admin / admin123")