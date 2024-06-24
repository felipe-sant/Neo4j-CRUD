from src.utils.formatarTexto import (formatarTexto_italico, formatarTexto_negrito,
    formatarTexto_vermelho)
from src.functions.pegarTodos import pegarTodos
from src.functions.pegarUm import pegarUm

def listarUsuario():
    try:
        id = input(f"Digite o {formatarTexto_negrito("ID")} do usuário: {formatarTexto_italico('(deixe em branco para listar todos) ')}")
        if id == "":
            usuarios = pegarTodos("Usuario")
            if usuarios is None:
                raise Exception("Nenhum usuário encontrado.")
            tamanhoTotal = len(usuarios)
            count = 0
            print()
            for usuario in usuarios:
                print(formatarTexto_italico(f"- Usuário {count + 1} de {tamanhoTotal} -"))
                print(usuario)
                input()
                count += 1
        else:
            usuario = pegarUm("Usuario", id)
            if usuario is not None:
                print()
                print(usuario)
                input()
            else:
                raise Exception("Usuário não encontrado.")

    except Exception as e:
        print(f"\nError in listarUsuario: {formatarTexto_vermelho(str(e))}")
        input()
        return
    except KeyboardInterrupt:
        return
    
# Path: src/functions/listarUsuario.py
