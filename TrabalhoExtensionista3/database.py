import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'admin_login'

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///descarte.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'sua-chave-secreta-aqui')
    
    db.init_app(app)
    login_manager.init_app(app)
    
    with app.app_context():
        db.create_all()
        
        from models import User
        if not User.query.filter_by(username='admin').first():
            admin_user = User(username=os.getenv('ADMIN_USERNAME', 'admin'), is_admin=True)
            admin_user.set_password(os.getenv('ADMIN_PASSWORD', 'admin123'))
            db.session.add(admin_user)
            db.session.commit()