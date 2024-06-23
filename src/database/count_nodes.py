from src.database.connection import driver

def count_nodes(collection: str) -> int:
    try:
        def count_query(tx):
            query = f"MATCH (u:{collection}) RETURN count(u) AS total"
            result = tx.run(query)
            record = result.single()
            return record["total"] if record else 0

        with driver.session() as session:
            total = session.read_transaction(count_query)
            return total
    except Exception as e:
        print(f"An error occurred while counting nodes in the collection '{collection}': {e}")
        return 
    except KeyboardInterrupt:
        print("Operation canceled by the user.")
        return

# Path: src/database/count.py