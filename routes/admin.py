from flask import Blueprint, render_template, request, redirect, url_for, flash

import sqlite3

import requests, os

from db import conectar_db



admin_bp = Blueprint('admin', __name__)


senha_certa = 'ayssa2025'


@admin_bp.route('/login_admin', methods=['GET'])
def mostrar_tela_login():
    return render_template('loginPainelAdministrativo.html')



@admin_bp.route('/login_admin', methods=['POST'])
def login_admin():
    senha = request.form.get('senhaAcesso')
    if senha == senha_certa:
       return redirect(url_for('admin.tela_administracao'))
    else:
        flash('Senha incorreta! Tente novamente.')
        return render_template('loginPainelAdministrativo.html')

@admin_bp.route('/adicionar_brownie', methods=['POST', 'GET'])
def tela_administracao():
    if request.method == 'POST':
        nome = request.form['nomeProduto']
        descricao = request.form['descricaoProduto']
        preco = request.form['precoProduto']
        imagem_url = request.form['urlImagem']
        if imagem_url:
            if imagem_url.startswith('http'):
                nome_arquivo = f"{nome.replace(' ', '_')}.jpg"
                caminho_arquivo = os.path.join('static', 'img', nome_arquivo)
                try:
                    img_data = requests.get(imagem_url).content
                    with open(caminho_arquivo, 'wb') as f:
                        f.write(img_data)
                    imagem = f"/static/img/{nome_arquivo}"
                except:
                    imagem = url_for('static', filename='img/brownie1.jpeg')
            else:
                imagem = f"/static/img/{imagem_url}"
        else:
            imagem = f"/static/img/{imagem_url}"
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
    conectar = conectar_db()
    cursor = conectar.cursor()
    cursor.execute("select * from brownie")
    brownies = cursor.fetchall()
    conectar.close()
    for brownie in brownies:
        print(brownie[1])
    return render_template('painelAdministrativo.html', brownies=brownies)


# @admin_bp.route('/remover_brownie', methods=['POST'])
# def remover_brownie():
#     id_brownie = request.form['ID']
#     nome = request.form['nomeProduto']
#     descricao = request.form['descricaoProduto']
#     preco = request.form['precoProduto']
#     imagem_url = request.form['urlImagem']
#     if imagem_url:
#         nome_arquivo = f"{nome.replace(' ', '_')}.jpg"
#         caminho_arquivo = os.path.join('static', 'img', nome_arquivo)
#         try:
#             img_data = requests.get(imagem_url).content
#             with open(caminho_arquivo, 'wb') as f:
#                 f.write(img_data)
#             imagem = f"/static/img/{nome_arquivo}"
#         except:
#             imagem = url_for('static', filename='img/brownie1.jpeg')
#     else:
#         imagem = url_for('static', filename='img/brownie1.jpeg')
#     disponivel = True   

#     conectar = conectar_db()
#     cursor = conectar.cursor()
#     cursor.execute('''
#     insert into brownie (nome, descricao, preco, imagem, disponivel)
#     values (?, ?, ?, ?, ?)''',
#     (nome, descricao, preco, imagem, disponivel))
#     conectar.commit()
#     conectar.close()
#     return render_template('painelAdministrativo.html', nome=nome, descricao=descricao, preco=preco, imagem=imagem)


