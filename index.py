from src.database.connection import driver
from src.layouts.menuPrincipal import menuPrincipal
from src.utils.limparTerminal import limparTerminal

def main():
    menuPrincipal()
    limparTerminal()
    driver.close()

if __name__ == "__main__":
    main()

# Path: index.py