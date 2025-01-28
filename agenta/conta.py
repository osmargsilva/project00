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
    
def update(email):
    contato = findByEmail(email)
    if contato:
        labels = ("id", "nome", "sobrenome","telefone", "email")
        contact = {}
        for i in range(len(contato[0])):
            contact[labels[i]] = contato[0][i]
        nome = input("presine enter para pular se não for atualizar nome: ") or contact["nome"]
        sobrenome = input("presine enter para pular se não for atualizar Sobrenome: ") or contact["sobrenome"]
        Email = input("presine enter para pular se não for atualizar Email: ") or contact["email"]
        telefone = input("presine enter para pular se não for atualizar Telefone: ") or contact["telefone"]

        conn = sq.connect('./agenta/agenta.db')
        curso = conn.cursor()

        contados = curso.execute(f"""UPDATE contatos
        SET nome = '{nome}', sobrenome = '{sobrenome}', telefone = '{telefone}' , email = '{Email}'
        WHERE id = {int(contact['id'])};
        """)
        conn.commit()
        curso.close()
        conn.close()
        contact = findByEmail(Email)
        
        print(f"Atualizado: {contact}")
    else:
        print("Contato não existe.")


def delete(email):
    contato = findByEmail(email)
    if contato:
        labels = ("id", "nome", "sobrenome","telefone", "email")
        contact = {}
        for i in range(len(contato[0])):
            contact[labels[i]] = contato[0][i]

        conn = sq.connect('./agenta/agenta.db')
        curso = conn.cursor()

        contados = curso.execute(f"""DELETE FROM contatos WHERE id = {int(contact['id'])}""")
        conn.commit()
        curso.close()
        conn.close()
        print(contados)
    else:
        print("Contato não existe.")