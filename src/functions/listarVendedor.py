from src.utils.formatarTexto import (formatarTexto_italico, formatarTexto_negrito,
    formatarTexto_vermelho)
from src.functions.pegarTodos import pegarTodos
from src.functions.pegarUm import pegarUm

def listarVendedor():
    try:
        id = input(f"Digite o {formatarTexto_negrito("ID")} do vendedor: {formatarTexto_italico('(deixe em branco para listar todos) ')}")
        if id == "":
            vendedores = pegarTodos("Vendedor")
            if vendedores is None:
                raise Exception("Nenhum vendedor encontrado.")
            tamanhoTotal = len(vendedores)
            count = 0
            print()
            for vendedor in vendedores:
                print(formatarTexto_italico(f"- Vendedor {count + 1} de {tamanhoTotal} -"))
                print(vendedor)
                input()
                count += 1      
        else:
            vendedor = pegarUm("Vendedor", id)
            if vendedor is not None:
                print()
                print(vendedor)
                input()
            else:
                raise Exception("Vendedor não encontrado.")
    except Exception as e:
        print(f"\nError in listarVendedor: {formatarTexto_vermelho(str(e))}")
        input()
        return
    except KeyboardInterrupt:
        return

# Path: src/functions/listarVendedor.py  