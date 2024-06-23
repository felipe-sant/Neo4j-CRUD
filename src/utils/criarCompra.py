from typing import Optional
from src.classes.compra import Compra
from src.utils.solicitarInput import solicitarInput
from src.utils.formatarTexto import (formatarTexto_italico, formatarTexto_negrito,
    formatarTexto_vermelho)

def criarCompra(isRequired: bool, compra: Compra = None) -> Optional[Compra]:
    try:
        diaCompraText = f"Digite o {formatarTexto_negrito("dia")} da compra: "
        mesCompraText = f"Digite o {formatarTexto_negrito("mês")} da compra: "
        anoCompraText = f"Digite o {formatarTexto_negrito("ano")} da compra: "
        if compra:
            diaCompraText = f"Digite o novo {formatarTexto_negrito('dia')} da compra {formatarTexto_italico(f'(atual: {compra.dataCompra.split("/")[0]})')}: "
            mesCompraText = f"Digite o novo {formatarTexto_negrito('mês')} da compra {formatarTexto_italico(f'(atual: {compra.dataCompra.split("/")[1]})')}: "
            anoCompraText = f"Digite o novo {formatarTexto_negrito('ano')} da compra {formatarTexto_italico(f'(atual: {compra.dataCompra.split("/")[2]})')}: "
        diaCompra = solicitarInput(diaCompraText, isRequired)
        if diaCompra == "" and compra:
            diaCompra = compra.dataCompra.split("/")[0]
        mesCompra = solicitarInput(mesCompraText, isRequired)
        if mesCompra == "" and compra:
            mesCompra = compra.dataCompra.split("/")[1]
        anoCompra = solicitarInput(anoCompraText, isRequired)
        if anoCompra == "" and compra:
            anoCompra = compra.dataCompra.split("/")[2]
        dataCompra = f"{diaCompra}/{mesCompra}/{anoCompra}"
        compra = Compra(dataCompra=dataCompra)
        compra.validate()
        return compra
    except Exception as e:
        print(f"\nErro ao criar compra: {formatarTexto_vermelho(str(e))}")
        input()
        return None
    except KeyboardInterrupt:
        return 
    
# Path: src/utils/criarCompra.py