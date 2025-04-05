from app.models import db
from datetime import datetime

class Perfil(db.Model):
    __tablename__ = 'perfiles'

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.String(36), db.ForeignKey('usuarios.id'), unique=True, nullable=False)
    rol = db.Column(db.String(50), nullable=False)
    estado_rostro = db.Column(db.String(50), nullable=False)
    creado_en = db.Column(db.DateTime, default=datetime.utcnow)
    telefono = db.Column(db.String(20))  # Campo adicional opcional

    usuario = db.relationship('Usuario', back_populates='perfil')

def to_dict(self):
    return {
        'rol': self.rol,
        'estado_rostro': self.estado_rostro,
        'creado_en': self.creado_en.isoformat(),
        'telefono': self.telefono
    }