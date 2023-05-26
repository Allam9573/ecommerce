from flask import Blueprint, render_template, request
from app.modules.db.db import get_connection
bp = Blueprint('auth', __name__, url_prefix='/users')


@bp.route('/login', methods=['POST', 'GET'])
def login():
    return render_template('auth/login.html')


@bp.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']
        telefono = request.form['telefono']
        contrasenia = request.form['contrasenia']
        conexion = get_connection()
        cursor = conexion.cursor(buffered=True)
        cursor.execute('INSERT usuarios(nombre,apellido,correo,telefono,contrasenia) VALUES(%s,%s,%s,%s,%s)',
                       (nombre, apellido, correo, telefono, contrasenia))
    return render_template('auth/register.html')
