from src.database.create_usuario import create_usuario
from src.database.search import search
from src.database.count import count
from src.database.connection import driver

result = count("Usuario")

print(result)

driver.close()