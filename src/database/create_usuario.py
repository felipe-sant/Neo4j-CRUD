from src.classes.usuario import Usuario
from src.database.connection import driver
from src.database.count_nodes import count_nodes

def create_usuario(usuario: Usuario) -> str:
    try:
        total = count_nodes("Usuario")
        userid = total + 1
        nome = usuario.nome
        endereco = usuario.endereco
        rg = usuario.rg
        
        def create_user(tx, userid, nome, endereco, rg):
            query = """
            CREATE (:Usuario {id: $userid, nome: $nome, endereco: $endereco, rg: $rg})
            """
            tx.run(query, userid=userid, nome=nome, endereco=endereco, rg=rg)
        
        with driver.session() as session:
            session.write_transaction(create_user, userid, nome, endereco, rg)
        
        return "Node created successfully!"
    except Exception as e:
        return f"Failed to create node: {e}"
    except KeyboardInterrupt:
        return "Operation canceled by the user."

# Path: src/database/create.py