from src.database.connection import driver
from src.database.count import count

def create_usuario(dados):
    try:
        total = count("Usuario")
        id, nome, endereco, rg = count+1, dados["nome"], dados["endereco"], dados["rg"]
        
        # Função para criar um usuário no banco de dados
        def create(tx, id, nome, endereco, rg):
            query = """
            CREATE (:Usuario {id: $id, nome: $nome, endereco: $endereco, rg: $rg})
            """
            tx.run(query, id=id, nome=nome, endereco=endereco, rg=rg)
        
        # Usar uma sessão para executar a transação
        with driver.session() as session:
            session.write_transaction(create, id, nome, endereco, rg)
        
        return "Node created successfully!"
    except Exception as e:
        return "Failed to create node: " + str(e)
    
# Path: src/database/create.py