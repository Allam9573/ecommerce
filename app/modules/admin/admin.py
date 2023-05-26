from flask import Flask, render_template, Blueprint

bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/')
def admin_root():
    return render_template('admin/admin.html')
