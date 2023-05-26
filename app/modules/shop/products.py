from app.modules.db.db import get_connection
from flask import Blueprint, render_template, request

bp = Blueprint('product', __name__, url_prefix='/shop')


@bp.route('/product/register_product', methods=['POST', 'GET'])
def register_product():
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        imagen = request.form['imagen']
        conexion = get_connection()
        cursor = conexion.cursor(buffered=True)
        cursor.execute(
            'INSERT INTO products(nombre,precio,imagen) VALUES(%s,%s,%s)', (nombre, precio, imagen))
        conexion.commit()

    return render_template('products/register_product.html')


@bp.route('/shop')
def list_products():
    conexion = get_connection()
    cursor = conexion.cursor(buffered=True)
    cursor.execute('SELECT * FROM products')
    conexion.commit()
    data = cursor.fetchall()
    return render_template('shop.html', data=data)
