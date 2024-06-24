from src.classes.usuario import Usuario
from src.database.connection import driver
from src.database.count_nodes import count_nodes
from src.utils.formatarTexto import formatarTexto_azul, formatarTexto_vermelho

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
        
        return f"{formatarTexto_azul("Nó criado com sucesso!")}"
    except Exception as e:
        return f"Falha ao criar nó: {formatarTexto_vermelho(str(e))}"
    except KeyboardInterrupt:
        return "Operação cancelada."

# Path: src/database/create.py