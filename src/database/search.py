from src.database.connection import driver

def search(colecao, filter = None):
    try:
        querry = "MATCH (u:" + colecao + ") RETURN u"
        if filter:
            querry = "MATCH (u:" + colecao + ") WHERE u." + filter + " RETURN u"
        with driver.session() as session:
            result = session.run(querry)
            dados = []
            for dado in result.data():
                dados.append(dado["u"])
            return dados
    except Exception as e:
        return "Failed to search node: " + str(e)

# Path: src/database/search_usuario.py    