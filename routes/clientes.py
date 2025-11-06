from flask import Blueprint, render_template, request, redirect, url_for

import sqlite3

from db import conectar_db

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