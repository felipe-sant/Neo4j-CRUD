from typing import Optional
from src.classes.produto import Produto
from src.utils.solicitarInput import solicitarInput
from src.utils.formatarTexto import (formatarTexto_italico, formatarTexto_negrito,
    formatarTexto_vermelho)

def criarProduto(isRequired: bool, produto: Produto = None) -> Optional[Produto]:
    try:
        nomeText = f"Digite o {formatarTexto_negrito('nome')} do produto: "
        descricaoText = f"Digite a {formatarTexto_negrito('descrição')} do produto: "
        precoText = f"Digite o {formatarTexto_negrito('preço')} do produto: "
        estoqueText = f"Digite o {formatarTexto_negrito('estoque')} do produto: "
        if produto:
            nomeText = f"Digite o novo {formatarTexto_negrito('nome')} do produto {formatarTexto_italico(f"(atual: {produto.nome})")}: "
            descricaoText = f"Digite a nova {formatarTexto_negrito('descrição')} do produto {formatarTexto_italico(f"(atual: {produto.descricao})")}: "
            precoText = f"Digite o novo {formatarTexto_negrito('preço')} do produto {formatarTexto_italico(f"(atual: {produto.preco})")}: "
            estoqueText = f"Digite o novo {formatarTexto_negrito('estoque')} do produto {formatarTexto_italico(f"(atual: {produto.estoque})")}: "
        nome = solicitarInput(nomeText, isRequired)
        descricao = solicitarInput(descricaoText, isRequired)
        preco = solicitarInput(precoText, isRequired)
        if preco: preco = float(preco)
        estoque = solicitarInput(estoqueText, isRequired)
        if estoque: estoque = int(estoque)
        produto = Produto(nome=nome, descricao=descricao, preco=preco, estoque=estoque)
        produto.validate()
        return produto
    except Exception as e:
        print(f"\nErro ao criar produto: {formatarTexto_vermelho(str(e))}")
        input()
        return None
    except KeyboardInterrupt:
        return None
        
# Path: src/utils/criarProduto.py