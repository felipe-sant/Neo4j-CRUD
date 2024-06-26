from src.classes.compra import Compra
from src.database.count_nodes import count_nodes
from src.database.connection import driver
from src.utils.formatarTexto import formatarTexto_azul, formatarTexto_vermelho

def insert_compra(compra: Compra) -> str:
    try:
        total = count_nodes("Compra")
        nodeid = total + 1
        dataCompra = compra.dataCompra
        
        def create_compra(tx, purchaseid, dataCompra):
            query = """
            CREATE (:Compra {id: $purchaseid, dataCompra: $dataCompra})
            """
            tx.run(query, purchaseid=purchaseid, dataCompra=dataCompra)
            
        with driver.session() as session:
            session.write_transaction(
                create_compra,
                purchaseid=nodeid,
                dataCompra=dataCompra
            )
        
        return f"{formatarTexto_azul('Nó criado com sucesso!')}"
    except Exception as e:
        return f"Falha ao criar nó: {formatarTexto_vermelho(str(e))}"
    except KeyboardInterrupt:
        return "Operação cancelada."
    
# Path: src/database/insert_compra.py