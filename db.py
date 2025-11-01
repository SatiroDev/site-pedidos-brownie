import sqlite3

def conectar_db():
    conectar = sqlite3.connect('brownie.db')
    conectar.execute("PRAGMA foreign_keys = ON")
    conectar.row_factory = sqlite3.Row
    return conectar