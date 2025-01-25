import conn
import conta
import os
import time

if not os.path.exists('./agenta/agenta.db'):
    conn.create_table()

def main():
    os.system('clear') or None
    title = """
=================== Agenta Pessoal ==================
    """
    menu = """
    [1] - Adicionar novo contato
    [2] - Consltar contados
    [3] - Atualizar contato
    [4] - Remover contato
    [0] - Sair
"""
    while True:
        print(title)
        print(menu)
        op= int(input("Informe um opção: "))
        os.system('clear') or None
        if op != 0:
            if op == 1:
                nome = input("* Digite o nome do novo contado: ")
                sobrenome = input("Sobrenome: ")
                email = input("* Email: ")
                telefone = input("* Telefone: ")
                if nome == "" or email == "" or telefone == "":
                    print("prencha os campos corretamente")
                else:
                    conta.createNewContact(nome, sobrenome, email, telefone)
                time.sleep(3)
                os.system('clear') or None
            elif op == 2:
                print("====== Contatos ========")
                email = input("Digite o email caso queira um contato especifico: ")
                if email == "":
                    conta.findByAll()
                else:
                    print(conta.findByEmail(email))
                time.sleep(5)
                os.system('clear') or None

        else:
            break

            
main()
