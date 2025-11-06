from flask import Blueprint, render_template, request, redirect, url_for

import sqlite3

import requests, os

from db import conectar_db

brownies_bp = Blueprint('brownies', __name__)

def criar_tabela_brownie():
    conectar = conectar_db()
    cursor = conectar.cursor()
    cursor.execute('''
        create table if not exists brownie (
            id integer primary key autoincrement,
            nome text not null,
            descricao text not null,
            preco decimal(5,2) not null,
            imagem text not null,
            disponivel boolean
    )''')
    conectar.commit()
    conectar.close()


# @brownies_bp.route('/listar_brownie', methods=['GET'])
# def nossos_produtos():
#     return render_template('nossosProdutos.html')

@brownies_bp.route('/listar_brownie', methods=['GET'])
def listar_brownies():
    conectar = conectar_db()
    cursor = conectar.cursor()
    cursor.execute("select * from brownie")
    brownies = cursor.fetchall()
    conectar.close()
    for brownie in brownies:
        for i in range(len(brownie)):

            print(brownie[i])

    return render_template('nossosProdutos.html', brownies=brownies)

