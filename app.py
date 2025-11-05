from flask import Flask


from flask import Flask, render_template, request, redirect, url_for, flash

import sqlite3

app = Flask(__name__)
app.secret_key = '101010'

# se conecta ao banco de dados
def conectar_db():
    conectar = sqlite3.connect('brownie.db')
    conectar.execute("PRAGMA foreign_keys = ON")
    return conectar

# cria a tabela cliente
def criar_tabela_cliente():
    conectar = conectar_db()
    cursor = conectar.cursor()
    cursor.execute('''
        create table if not exists cliente (
            id integer primary key autoincrement,
            nome text not null,
            telefone text not null,
            endereco text not null,
            data_criacao datetime
    )''')
    conectar.commit()
    conectar.close()

# cria a tabela brownie
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

# cria a tabela pedido
def criar_tabela_pedido():
    conectar = conectar_db()
    cursor = conectar.cursor()
    cursor.execute('''
        id integer primary key autoincrement,
        cliente_id integer not null,
        date_pedido datetime default current_timestamp,
        total decimal(6,2),
        status text defalt 'pedente',
        foreign key (cliente_id) references cliente(id)
    ''')
    conectar.commit()
    conectar.close()

# cria tabela pedido_item
def criar_tabela_pedido_item():
    conectar = conectar_db()
    cursor = conectar.cursor()
    cursor.execute('''
        id integer primary key autoincrement,
        pedido_id integer not null,
        brownie_id integer not null,
        quantidade integer,
        preco_unitario decimal(5,2) not null
                       
    ''')
    conectar.commit()
    conectar.close()

# @app.route('/')
# def index():
#     return render_template('index.html')


