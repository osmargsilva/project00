import sqlite3 as sq

def findByAll():
    conn = sq.connect('./agenta/agenta.db')
    curso = conn.cursor()

    contados = curso.execute("""SELECT * FROM contatos""").fetchall()
    conn.commit()
    curso.close()
    conn.close()
    for contado in contados:
        print(contado)

def findByEmail(email):
    conn = sq.connect('./agenta/agenta.db')
    curso = conn.cursor()

    contado = curso.execute(f""" 
        SELECT * FROM contatos WHERE email='{email}'
    """).fetchall()
    conn.commit()
    curso.close()
    conn.close()
    return contado

def createNewContact(nome, sobrenome, email, telefone ):
    contado = findByEmail(email)
    
    if not contado:
        conn = sq.connect('./agenta/agenta.db')
        cursor = conn.cursor()
        cursor.execute(f""" 
        INSERT INTO contatos (nome, sobrenome, telefone, email)
                    VALUES ('{nome}', '{sobrenome}', '{telefone}', '{email}')
        """)
        conn.commit()
        cursor.close()
        conn.close()
        print('Contato Salvo com sucesso')
    else:
        print('O contato ja existe na agenta')
        