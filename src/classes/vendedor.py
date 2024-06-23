from dataclasses import dataclass, field, asdict
from src.classes.produto import Produto

@dataclass
class Vendedor:
    _id: str = field(default=None, repr=False)
    nome: str = field(default="")
    rg: str = field(default="")
    produtos: list[dict[str, any]] = field(default_factory=list)
    
    def __str__(self) -> str:
        listagem = ""
        listagem += f"_id: {self._id}\n" if self._id is not None else ""
        listagem += f"nome: {self.nome}\n" if self.nome != "" else ""
        listagem += f"rg: {self.rg}\n" if self.rg != "" else ""
        if self.produtos != []:
            count = len(self.produtos)
            listagem += "produtos:\n"
            for produto in self.produtos:
                count -= 1
                listagem += f"\tid: {produto['id']}\n" if produto.get("id", None) else ""
                listagem += f"\tnome: {produto['nome']}\n" if produto.get("nome", None) else ""
                listagem += f"\tpreco: {produto['preco']}\n" if produto.get("preco", None) else ""
                if count != 0:
                    listagem += "\t-----------------\n"
        return listagem
    
    def addProduto(self, produto: Produto) -> None:
        newProduto = {
            "id": produto._id,
            "nome": produto.nome,
            "preco": produto.preco
        }
        if newProduto not in self.produtos:
            self.produtos.append(newProduto)
        
    def removeProduto(self, _id: str) -> None:
        for produto in self.produtos:
            if produto.get("id", None) == _id:
                self.produtos.remove(produto)
                break
    
    def toDict(self) -> dict:
        result = asdict(self)
        return {k: v for k, v in result.items() if v != None and v != '' and v != []}
    
    @classmethod
    def fromDict(cls, vendedorJson: dict) :
        return cls(
            _id = vendedorJson.get("_id", None),
            nome = vendedorJson.get("nome", ""),
            rg = vendedorJson.get("rg", ""),
            produtos = vendedorJson.get("produtos", [])
        )
        
    def validate(self) -> None:
        if self._id is not None and not isinstance(self._id, str):
            raise ValueError("id deve ser uma string")
        if not isinstance(self.nome, str):
            raise ValueError("nome deve ser uma string")
        if not isinstance(self.rg, str):
            raise ValueError("rg deve ser uma string")
        if not isinstance(self.produtos, list):
            raise ValueError("produtos deve ser uma lista")
        for produto in self.produtos:
            if not isinstance(produto, dict):
                raise ValueError("produtos deve ser uma lista de dicionários")
            
# Path: src/classes/vendedor.py