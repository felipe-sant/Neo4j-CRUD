from src.utils.formatarTexto import formatarTexto_azul, formatarTexto_vermelho
from src.database.connection import driver

def create_relation(primeiroNó: str, segundoNó: str, nomeDaRelacao: str) -> str | None:
    try:
        querry = f'''
        MATCH (a:{primeiroNó}), (b:{segundoNó}) CREATE (a)-[:{nomeDaRelacao}]->(b)
        '''
        with driver.session() as session:
            session.run(querry)
            return f"{formatarTexto_azul("Relação criada com sucesso!")}"
    except Exception as e:
        return None
    except KeyboardInterrupt:
        return None