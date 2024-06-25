from src.utils.criarUsuario import criarUsuario
from src.database.insert_usuario import insert_usuario
from src.utils.formatarTexto import formatarTexto_vermelho

def cadastrarUsuario():
    try:
        usuario = criarUsuario(isRequired=True)
        result = insert_usuario(usuario)
        print()
        print(result)
        input()
    except Exception as e:
        print(f"\nFalha ao cadastrar usuário: {formatarTexto_vermelho(str(e))}")
        input()
        return
    except KeyboardInterrupt:
        return

# Path: src/functions/cadastrarUsuario.py
    