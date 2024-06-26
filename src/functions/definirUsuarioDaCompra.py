from src.database.create_relation import create_relation
from src.utils.formatarTexto import formatarTexto_vermelho
from src.classes.usuario import Usuario
from src.classes.compra import Compra

def definirUsuarioDaCompra(usuario: Usuario, compra: Compra):
    try:
        usuario = "Usuario {id: " + str(usuario.id) + "}"
        compra = "Compra {id: " + str(compra.id) + "}"
        result = create_relation(usuario, compra, "FEZ")
        if result:
            print()
            print(result)
            input()
    except Exception as e:
        print(f"Erro ao criar relação: {formatarTexto_vermelho(str(e))}\n")
        input()
    except KeyboardInterrupt:
        return
    
# Path: src/functions/definirUsuarioDaCompra.py