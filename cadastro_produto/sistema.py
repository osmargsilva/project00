import os
import time
import core

users = []

while True:
    os.system('clear') or None
    print("""
[1] - Novo Usuario
    [2] - Busca Usuario
        [0] - Fecha o sistema
    """)
    op = int(input("Infome a opção: "))

    if op !=0:
        os.system('clear') or None
        if op == 1:
            core.createUser()
            time.sleep(3)
            os.system('clear') or None
        elif op == 2:
            os.system('clear') or None
            core.selectUsers()
            time.sleep(3)
            os.system('clear') or None
        else:
            print(f'opção invalida')
            time.sleep(2)
            os.system('clear') or None
    else:
        os.system('clear') or None
        break
    