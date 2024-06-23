from src.database.connection import driver
from typing import List, Dict, Any, Optional

def search_nodes(collection: str, filter: Optional[str] = None) -> Optional[List[Dict[str, Any]]]:
    try:
        query = f"MATCH (u:{collection})"
        if filter:
            query += f" WHERE u.{filter}"
        query += " RETURN u"

        with driver.session() as session:
            result = session.run(query)
            nodes = [record["u"] for record in result]
        
        return nodes
    except Exception as e:
        print(f"Failed to search node: {e}")
        return None
    except KeyboardInterrupt:
        print("Operation canceled by the user.")
        return None

# Path: src/database/search_usuario.py