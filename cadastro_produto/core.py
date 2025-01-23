import psycopg2 as psq

def selectUsers():
    conn = psq.connect(
        database = "cursoPy",
        user = "gomes",
        host= '147.79.111.150',
        password = "gomes123",
        port = 5435
    )
    cur = conn.cursor()
    cur.execute('SELECT * FROM produtos;')
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)

def createUser():
    conn = psq.connect(
        database = "cursoPy",
        user = "gomes",
        host= '147.79.111.150',
        password = "gomes123",
        port = 5435
    )
    produto = input("digite um produto: ")
    if produto != "":
        code= input("digite um code: ")
        preco= float(input("digite um preco: "))
        qtd= int(input("digite um qtd: "))
    cur = conn.cursor()
    cur.execute(f"INSERT INTO produtos (codido, produto, quantidade, preco_unid) VALUES('{code}','{produto}',{qtd}, {preco})");
    conn.commit()
    conn.close()
    print("Cadastro realizado!")