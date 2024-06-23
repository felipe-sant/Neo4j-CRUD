from dataclasses import dataclass, field, asdict
from src.classes.produto import Produto
from src.classes.usuario import Usuario

@dataclass
class Compra:
    _id: str = field(default=None, repr=False)
    dataCompra: str = field(default="")
    valorTotal: float = field(default=0.0)
    usuario: dict[str, any] = field(default_factory=dict)
    produtos: list[dict[str, any]] = field(default_factory=list)
    
    def __str__(self) -> str:
        listagem = ""
        listagem += f"_id: {self._id}\n" if self._id is not None else ""
        listagem += f"dataCompra: {self.dataCompra}\n" if self.dataCompra != "" else ""
        listagem += f"valorTotal: {self.valorTotal}\n" if self.valorTotal != 0.0 else ""
        if self.usuario:
            listagem += "usuario:\n"
            listagem += f"\t_id: {self.usuario['id']}\n" if self.usuario.get("id", None) else ""
            listagem += f"\tnome: {self.usuario['nome']}\n" if self.usuario.get("nome", None) else ""
        if self.produtos != []:
            count = len(self.produtos)
            listagem += "produtos:\n"
            for produto in self.produtos:
                count -= 1
                listagem += f"\t_id: {produto['id']}\n" if produto.get("id", None) else ""
                listagem += f"\tnome: {produto['nome']}\n" if produto.get("nome", None) else ""
                listagem += f"\tpreco: {produto['preco']}\n" if produto.get("preco", None) else ""
                if count != 0:
                    listagem += "\t-----------------\n"
        return listagem
    
    def calcularValorTotal(self):
        valorTotal = 0.0
        for produto in self.produtos:
            valorTotal += produto.get("preco", 0.0)
        self.valorTotal = valorTotal
    
    def setUsuario(self, usuario: Usuario) -> None:
        newUsuario = {
            "id": usuario._id,
            "nome": usuario.nome
        }
        self.usuario = newUsuario
    
    def addProduto(self, produto: Produto) -> None:
        newProduto = {
            "id": produto._id,
            "nome": produto.nome,
            "preco": produto.preco
        }
        self.produtos.append(newProduto)
    
    def removeProduto(self, _id: str) -> None:
        for produto in self.produtos:
            if produto.get("id", None) == _id:
                self.produtos.remove(produto)
                break
    
    def toDict(self) -> dict:
        result = asdict(self)
        return {k: v for k, v in result.items() if v != None and v != '' and v != 0.0 and v != 0 and v != {} and v != []}
    
    @classmethod
    def fromDict(cls, compraJson: dict) :
        return cls(
            _id = compraJson.get("_id", None),
            dataCompra = compraJson.get("dataCompra", ""),
            valorTotal = compraJson.get("valorTotal", 0.0),
            usuario = compraJson.get("usuario", {}),
            produtos = compraJson.get("produtos", [])
        )
        
    def validate(self) -> None:
        if self._id is not None and not isinstance(self._id, str):
            raise ValueError("id deve ser uma string")
        if not isinstance(self.dataCompra, str):
            raise ValueError("dataCompra deve ser uma string")
        if not isinstance(self.valorTotal, float):
            raise ValueError("valorTotal deve ser um float")
        if not isinstance(self.usuario, dict):
            raise ValueError("usuario deve ser um dicionário")
        if self.usuario:
            if self.usuario.get("_id", None) is not None and not isinstance(self.usuario["_id"], str):
                raise ValueError("usuario['_id'] deve ser uma string")
            if not isinstance(self.usuario.get("nome", ""), str):
                raise ValueError("usuario['nome'] deve ser uma string")
        if not isinstance(self.produtos, list):
            raise ValueError("produtos deve ser uma lista")
        for produto in self.produtos:
            if not isinstance(produto, dict):
                raise ValueError("produtos deve ser uma lista de dicionários")
    
# Path: src/classes/compra.py
    