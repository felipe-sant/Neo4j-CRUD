from src.utils.formatarTexto import (formatarTexto_italico, formatarTexto_negrito,
    formatarTexto_vermelho)
from src.functions.pegarUm import pegarUm
from src.functions.pegarTodos import pegarTodos

def listarCompra():
    try:
        id = input(f"Digite o {formatarTexto_negrito('ID')} da compra: {formatarTexto_italico('(deixe em branco para listar todas) ')}")
        if id == "":
            compras = pegarTodos("Compra")
            if compras is None:
                raise Exception("Nenhuma compra encontrada.")
            tamanhoTotal = len(compras)
            count = 0
            print()
            for compra in compras:
                print(formatarTexto_italico(f"- Compra {count + 1} de {tamanhoTotal} -"))
                print(compra)
                input()
                count += 1
        else:
            compra = pegarUm("Compra", id)
            if compra is not None:
                print()
                print(compra)
                input()
            else:
                raise Exception("Compra não encontrada.")
    except Exception as e:
        print(f"\nError in listarCompra: {formatarTexto_vermelho(str(e))}")
        input()
        return
    except KeyboardInterrupt:
        return
    
# Path: src/functions/listarCompra.py