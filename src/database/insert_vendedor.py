from src.classes.vendedor import Vendedor
from src.database.count_nodes import count_nodes
from src.database.connection import driver
from src.utils.formatarTexto import formatarTexto_azul, formatarTexto_vermelho

def insert_vendedor(vendedor: Vendedor) -> str:
    try:
        total = count_nodes("Vendedor")
        nodeid = total + 1
        nome = vendedor.nome
        rg = vendedor.rg
        
        def create_vendedor(tx, sellerid, nome, rg):
            querry = """
            CREATE (:Vendedor {id: $sellerid, nome: $nome, rg: $rg})
            """
            tx.run(querry, sellerid=sellerid, nome=nome, rg=rg)
            
        with driver.session() as session:
            session.write_transaction(
                create_vendedor,
                sellerid=nodeid,
                nome=nome,
                rg=rg
            )
            
        return f"{formatarTexto_azul('Nó criado com sucesso!')}"
    except Exception as e:
        return f"Falha ao criar nó: {formatarTexto_vermelho(str(e))}"
    except KeyboardInterrupt:
        return "Operação cancelada."
    
# Path: src/database/insert_vendedor.py