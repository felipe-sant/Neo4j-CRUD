from src.utils.criarVendedor import criarVendedor
from src.database.insert_vendedor import insert_vendedor
from src.utils.formatarTexto import formatarTexto_vermelho

def cadastrarVendedor():
    try:
        vendedor = criarVendedor(isRequired=True)
        result = insert_vendedor(vendedor)
        print()
        print(result)
        input()
    except Exception as e:
        print(f"\nFalha ao cadastrar vendedor: {formatarTexto_vermelho(str(e))}")
        input()
        return
    except KeyboardInterrupt:
        return

# Path: src/functions/cadastrarVendedor.py