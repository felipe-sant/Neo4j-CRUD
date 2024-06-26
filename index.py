from src.database.connection import driver
from src.layouts.menuPrincipal import menuPrincipal
from src.utils.limparTerminal import limparTerminal
from src.database.create_relation import create_relation

def main():
    menuPrincipal()
    limparTerminal()
    driver.close()

if __name__ == "__main__":
    main()

# Path: index.py