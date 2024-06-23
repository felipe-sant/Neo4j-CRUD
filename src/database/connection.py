from neo4j import GraphDatabase

uri = "neo4j+s://dd585e27.databases.neo4j.io:7687"
auth = ("neo4j", "jbq7Gbx0HaVqZQAWZJ5mktc5T9WftmGdMFnDkhFcWz0")

driver = GraphDatabase.driver(
    uri=uri, 
    auth=auth,
    max_connection_lifetime=30,  # Tempo máximo de vida da conexão (em segundos)
    max_connection_pool_size=50,  # Tamanho máximo do pool de conexões
    connection_timeout=15  # Tempo limite de conexão (em segundos)
)

# Path: src/database/connection.py