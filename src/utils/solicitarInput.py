from src.utils.formatarTexto import formatarTexto_amarelo

def solicitarInput(prompt: str, isRequired: bool = False) -> str | None:
    while True:
        valor = input(prompt).strip()
        if isRequired and not valor:
            print(formatarTexto_amarelo("Valor não pode ser vazio"))
            continue
        else:
            return valor
        
# Path: src/utils/solicitarInput.py