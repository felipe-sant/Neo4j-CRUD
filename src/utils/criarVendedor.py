from typing import Optional
from src.classes.vendedor import Vendedor
from src.utils.solicitarInput import solicitarInput
from src.utils.formatarTexto import (formatarTexto_italico, formatarTexto_negrito,
    formatarTexto_vermelho)

def criarVendedor(isRequired: bool, vendedor: Vendedor = None) -> Optional[Vendedor]:
    try:
        nomeText = f"Digite o {formatarTexto_negrito("nome")} do vendedor: "
        rgText = f"Digite o {formatarTexto_negrito("rg")} do vendedor: "
        if vendedor:
            nomeText = f"Digite o novo {formatarTexto_negrito('nome')} do vendedor {formatarTexto_italico(f"(atual: {vendedor.nome})")}: "
            rgText = f"Digite o novo {formatarTexto_negrito('rg')} do vendedor {formatarTexto_italico(f"(atual: {vendedor.rg})")}: "
        nome = solicitarInput(nomeText, isRequired)
        rg = solicitarInput(rgText, isRequired)
        vendedor = Vendedor(nome=nome, rg=rg, produtos=[])
        vendedor.validate()
        return vendedor
    except Exception as e:
        print(f"\nErro ao criar vendedor: {formatarTexto_vermelho(str(e))}")
        input()
        return None
    except KeyboardInterrupt:
        return None
    
# Path: src/utils/criarVendedor.py