from src.classes.usuario import Usuario
from src.database.connection import driver
from src.database.count_nodes import count_nodes

def create_usuario(usuario: Usuario) -> str:
    try:
        total = count_nodes("Usuario")
        user_id = total + 1
        nome = usuario.nome
        endereco = usuario.endereco
        rg = usuario.rg
        
        def create_user(tx, user_id, nome, endereco, rg):
            query = """
            CREATE (:Usuario {id: $user_id, nome: $nome, endereco: $endereco, rg: $rg})
            """
            tx.run(query, user_id=user_id, nome=nome, endereco=endereco, rg=rg)
        
        with driver.session() as session:
            session.write_transaction(create_user, user_id, nome, endereco, rg)
        
        return "Node created successfully!"
    except Exception as e:
        return f"Failed to create node: {e}"
    except KeyboardInterrupt:
        return "Operation canceled by the user."

# Path: src/database/create.py