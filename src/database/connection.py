from neo4j import GraphDatabase

uri = "neo4j+s://e8f76211.databases.neo4j.io"
auth = ("neo4j", "xhxov6nnL0M7o7VomqQpYkxxXas1Q2k3EcZZiv_d3xI")

driver = GraphDatabase.driver(
    uri=uri, 
    auth=auth,
    max_connection_lifetime=30,  # Tempo máximo de vida da conexão (em segundos)
    max_connection_pool_size=50,  # Tamanho máximo do pool de conexões
    connection_timeout=15  # Tempo limite de conexão (em segundos)
)

# Path: src/database/connection.py