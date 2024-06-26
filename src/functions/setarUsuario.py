from src.functions.pegarUm import pegarUm
from src.classes.compra import Compra
from src.functions.definirProdutoDaCompra import definirProdutoDaCompra
from src.utils.formatarTexto import formatarTexto_vermelho
from src.functions.definirUsuarioDaCompra import definirUsuarioDaCompra

def setarUsuario(compra: Compra):
    try:
        id = input("Digite o id do usuario: ")
        usuario = pegarUm("Usuario", id)
        if usuario:
            definirUsuarioDaCompra(usuario, compra)
            return
        else:
            raise Exception("Usuário não encontrado")
    except Exception as e:
        print(f"Erro ao setar usuário: {formatarTexto_vermelho(str(e))}")
        input()
    except KeyboardInterrupt:
        return
    
# Path: src/functions/setarUsuario.py