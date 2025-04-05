from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app):
    db.init_app(app)

    with app.app_context():
        from app.models.usuario import Usuario
        from app.models.perfil import Perfil
        db.create_all()        
