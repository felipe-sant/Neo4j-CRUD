from src.classes.produto import Produto
from src.database.count_nodes import count_nodes
from src.database.connection import driver
from src.utils.formatarTexto import formatarTexto_azul, formatarTexto_vermelho

def insert_produto(produto: Produto) -> str:
    try:
        total = count_nodes("Produto")
        nodeid = total + 1
        nome = produto.nome
        descricao = produto.descricao
        preco = produto.preco
        estoque = produto.estoque
        
        def create_produto(tx, productid, nome, descricao, preco, estoque):
            query = """
            CREATE (:Produto {id: $productid, nome: $nome, descricao: $descricao, preco: $preco, estoque: $estoque})
            """
            tx.run(query, productid=productid, nome=nome, descricao=descricao, preco=preco, estoque=estoque)
            
        with driver.session() as session:
            session.write_transaction(
                create_produto,
                productid=nodeid,
                nome=nome,
                descricao=descricao,
                preco=preco,
                estoque=estoque
            )
        
        return f"{formatarTexto_azul('Nó criado com sucesso!')}"
    except Exception as e:
        return f"Falha ao criar nó: {formatarTexto_vermelho(str(e))}"
    except KeyboardInterrupt:
        return "Operação cancelada."

# Path: src/database/insert_produto.py