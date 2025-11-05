from flask import Blueprint, render_template, request, redirect

import sqlite3

from db import conectar_db

brownies_bp = Blueprint('brownies', __name__)

def conectar_db():
    conectar = sqlite3.connect('brownie.db')
    conectar.execute("PRAGMA foreign_keys = ON")
    return conectar

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

@brownies_bp.route('/brownies')
def listar_brownies():
    conectar = conectar_db()
    cursor = conectar.cursor()
    cursor.execute("select * from brownie")
    brownies = cursor.fetchall()
    conectar.close()
    return render_template('nossosProdutos.html', brownies=brownies)

@brownies_bp.route('/adicionar_brownie')
def adicionar_brownie():
    nome = request.form['nomeProduto']
    descricao = request.form['descricaoProduto']
    preco = request.form['precoProduto']
    imagem = request.form['urlImagem']
    if not imagem:
        imagem = '../img/brownie1.jpeg'
    disponivel = True   

    conectar = conectar_db()
    cursor = conectar.cursor()
    cursor.execute('''
    insert into brownie (nome, descricao, preco, imagem, disponivel)
    values (?, ?, ?, ?, ?)''',
    (nome, descricao, preco, imagem, disponivel))
    conectar.commit()
    conectar.close()
    return render_template('painelAdministrativo.html', nome=nome, descricao=descricao, preco=preco, imagem=imagem)
