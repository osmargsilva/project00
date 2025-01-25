import sqlite3 as sq

def create_table():
    conn = sq.connect('./agenta/agenta.db')
    cursor = conn.cursor()
    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS contatos (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        sobrenome TEXT NOT NULL,
        telefone TEXT NOT NULL,
        email TEXT NOT NULL
    )
    """)

    conn.commit()
    cursor.close()
    conn.close()