from flask import Blueprint, render_template, request, redirect

from db import conectar_db

brownies_bp = Blueprint('brownies', __name__)

@brownies_bp.route('/brownies')
def listar_brownies():
    conectar = conectar_db()
    cursor = conectar.cursor()
    cursor.execute("select * from brownie")
    brownies = cursor.fetchall()
    conectar.close()
    return render_template('nossosProdutos.html', brownies=brownies)

