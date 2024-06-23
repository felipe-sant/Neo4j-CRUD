from src.database.connection import driver

def count(colecao: str):
    try:
        # Função para contar os nós de uma coleção
        def count_querry(tx):
            querry = "MATCH (u:" + colecao + ") RETURN count(u) AS total"
            result = tx.run(querry)
            record = result.single()
            return record["total"] if record else 0
        
        # Usar uma sessão para executar a transação
        with driver.session() as session:
            total = session.read_transaction(count_querry)
            return total
    except Exception as e:
        print(e)
        return 0
    
# Path: src/database/count.py    