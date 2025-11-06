from flask import Blueprint, render_template, request, redirect, url_for

import sqlite3

from db import conectar_db


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