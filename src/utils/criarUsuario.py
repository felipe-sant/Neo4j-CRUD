from src.classes.usuario import Usuario
from src.utils.solicitarInput import solicitarInput
from typing import Optional
from src.utils.formatarTexto import (formatarTexto_italico, formatarTexto_negrito,
    formatarTexto_vermelho)

def criarUsuario(isRequired: bool, usuario: Usuario = None) -> Optional[Usuario]:
    try:
        nomeText = f"Digite o {formatarTexto_negrito("nome")} do usuário: "
        rgText = f"Digite o {formatarTexto_negrito("rg")} do usuário: "
        enderecoText = f"Digite o {formatarTexto_negrito("endereço")} do usuário: "
        if usuario:
            nomeText = f"Digite o novo {formatarTexto_negrito('nome')} do usuário {formatarTexto_italico(f"(atual: {usuario.nome})")}: "
            rgText = f"Digite o novo {formatarTexto_negrito('rg')} do usuário {formatarTexto_italico(f"(atual: {usuario.rg})")}: "
            enderecoText = f"Digite o novo {formatarTexto_negrito('endereço')} do usuário {formatarTexto_italico(f"(atual: {usuario.endereco})")}: "
        nome = str(solicitarInput(nomeText, isRequired)).lower()
        endereco = str(solicitarInput(enderecoText, isRequired)).lower()
        rg = str(solicitarInput(rgText, isRequired)).lower()
        usuario = Usuario(nome=nome, endereco=endereco, rg=rg)
        usuario.validate()
        return usuario
    except Exception as e:
        print(f"\nErro ao criar usuário: {formatarTexto_vermelho(str(e))}")
        input()
        return None
    except KeyboardInterrupt:
        return None
    
# Path: src/utils/criarUsuario.py