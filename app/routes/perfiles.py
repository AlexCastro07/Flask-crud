from flask import Blueprint, request, jsonify
from app.models.usuario import Usuario, db
from app.models.perfil import Perfil

perfiles_bp = Blueprint('perfiles_bp', __name__)

# Crear perfil para un usuario
@perfiles_bp.route('/usuarios/<id>/perfil', methods=['POST'])
def crear_perfil(id):
    usuario = Usuario.query.get(id)
    if not usuario:
        return jsonify({'error': 'Usuario no encontrado'}), 404

    if usuario.perfil:
        return jsonify({'error': 'Este usuario ya tiene un perfil'}), 400

    data = request.get_json()
    perfil = Perfil(
        usuario_id=id,
        rol=data['rol'],
        estado_rostro=data['estado_rostro'],
        telefono=data.get('telefono')
    )
    db.session.add(perfil)
    db.session.commit()
    return jsonify(perfil.to_dict()), 201

# Obtener el perfil de un usuario
@perfiles_bp.route('/usuarios/<id>/perfil', methods=['GET'])
def obtener_perfil(id):
    usuario = Usuario.query.get(id)
    if not usuario or not usuario.perfil:
        return jsonify({'error': 'Perfil no encontrado'}), 404

    return jsonify(usuario.perfil.to_dict())

# Actualizar el perfil de un usuario
@perfiles_bp.route('/usuarios/<id>/perfil', methods=['PUT'])
def actualizar_perfil(id):
    usuario = Usuario.query.get(id)
    if not usuario or not usuario.perfil:
        return jsonify({'error': 'Perfil no encontrado'}), 404

    data = request.get_json()
    perfil = usuario.perfil
    perfil.rol = data.get('rol', perfil.rol)
    perfil.estado_rostro = data.get('estado_rostro', perfil.estado_rostro)
    perfil.telefono = data.get('telefono', perfil.telefono)

    db.session.commit()
    return jsonify(perfil.to_dict())

# Eliminar el perfil de un usuario
@perfiles_bp.route('/usuarios/<id>/perfil', methods=['DELETE'])
def eliminar_perfil(id):
    usuario = Usuario.query.get(id)
    if not usuario or not usuario.perfil:
        return jsonify({'error': 'Perfil no encontrado'}), 404

    db.session.delete(usuario.perfil)
    db.session.commit()
    return jsonify({'mensaje': 'Perfil eliminado correctamente'})
