from dataclasses import dataclass, field, asdict

@dataclass
class Produto:
    _id: str = field(default=None, repr=False)
    nome: str = field(default="")
    descricao: str = field(default="")
    preco: float = field(default=0.0)
    estoque: int = field(default=0)
    vendedor: dict[str, any] = field(default_factory=dict)
    
    def __str__(self) -> str:
        listagem = ""
        listagem += f"_id: {self._id}\n" if self._id is not None else ""
        listagem += f"nome: {self.nome}\n" if self.nome != "" else ""
        listagem += f"descricao: {self.descricao}\n" if self.descricao != "" else ""
        listagem += f"preco: {self.preco}\n" if self.preco != 0.0 else ""
        listagem += f"estoque: {self.estoque}\n" if self.estoque != 0 else ""
        if self.vendedor:
            listagem += "vendedor:\n"
            listagem += f"\tid: {self.vendedor['id']}\n" if self.vendedor.get("id", None) else ""
            listagem += f"\tnome: {self.vendedor['nome']}\n" if self.vendedor.get("nome", None) else ""
        return listagem
    
    def toDict(self) -> dict:
        result = asdict(self)
        return {k: v for k, v in result.items() if v != None and v != '' and v != 0.0 and v != 0 and v != {}}
    
    @classmethod
    def fromDict(cls, produtoJson: dict) :
        return cls(
            _id = produtoJson.get("_id", None),
            nome = produtoJson.get("nome", ""),
            descricao = produtoJson.get("descricao", ""),
            preco = produtoJson.get("preco", 0.0),
            estoque = produtoJson.get("estoque", 0),
            vendedor = produtoJson.get("vendedor", {})
        )
        
    def validate(self) -> None:
        if self._id is not None and not isinstance(self._id, str):
            raise ValueError("id deve ser uma string")
        if not isinstance(self.nome, str):
            raise ValueError("nome deve ser uma string")
        if not isinstance(self.descricao, str):
            raise ValueError("descricao deve ser uma string")
        if not isinstance(self.preco, float) and self.preco != "" and self.preco != None:
            raise ValueError("preco deve ser um float")
        if not isinstance(self.estoque, int) and self.estoque != "" and self.estoque != None:
            raise ValueError("estoque deve ser um int")
        if not isinstance(self.vendedor, dict):
            raise ValueError("vendedor deve ser um dicionário")
        if self.vendedor:
            if self.vendedor.get("_id", None) is not None and not isinstance(self.vendedor["_id"], str):
                raise ValueError("vendedor['_id'] deve ser uma string")
            if not isinstance(self.vendedor.get("nome", ""), str):
                raise ValueError("vendedor['nome'] deve ser uma string")
            
# Path: src/classes/produto.py