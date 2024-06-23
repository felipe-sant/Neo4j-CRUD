from dataclasses import dataclass, field, asdict
from src.classes.produto import Produto

@dataclass
class Usuario:
    _id: str = field(default=None, repr=False)
    nome: str = field(default="")
    endereco: str = field(default="")
    rg: str = field(default="")
    favoritos: list[dict[str, any]] = field(default_factory=list)
    
    def __str__(self) -> str:
        listagem = ""
        listagem += f"_id: {self._id}\n" if self._id is not None else ""
        listagem += f"nome: {self.nome}\n" if self.nome != "" else ""
        listagem += f"endereco: {self.endereco}\n" if self.endereco != "" else ""
        listagem += f"rg: {self.rg}\n" if self.rg != "" else ""
        if self.favoritos != []:
            count = len(self.favoritos)
            listagem += "favoritos:\n"
            for produto in self.favoritos:
                count += 1
                listagem += f"\t_id: {produto['_id']}\n" if produto.get("_id", None) else ""
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
        self.favoritos.append(newProduto)
    
    def removeProduto(self, _id: str) -> None:
        for produto in self.favoritos:
            if produto.get("id", None) == _id:
                self.favoritos.remove(produto)
                break
    
    def toDict(self) -> dict:
        result = asdict(self)
        return {k: v for k, v in result.items() if v != None and v != '' and v != []}
    
    @classmethod
    def fromDict(cls, usuarioJson: dict) :
        return cls(
            _id = usuarioJson.get("_id", None),
            nome = usuarioJson.get("nome", ""),
            endereco = usuarioJson.get("endereco", ""),
            rg = usuarioJson.get("rg", ""),
            favoritos = usuarioJson.get("favoritos", [])
        )
        
    def validate(self) -> None:
        if self._id is not None and not isinstance(self._id, str):
            raise ValueError("id deve ser uma string")
        if not isinstance(self.nome, str):
            raise ValueError("nome deve ser uma string")
        if not isinstance(self.endereco, str):
            raise ValueError("endereco deve ser uma string")
        if not isinstance(self.rg, str):
            raise ValueError("rg deve ser uma string")
        if not isinstance(self.favoritos, list):
            raise ValueError("favoritos deve ser uma lista")
        for produto in self.favoritos:
            if not isinstance(produto, dict):
                raise ValueError("favorito deve ser uma lista de dicionários")
    
# Path: src/classes/usuario.py
