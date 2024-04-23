class InMemoryDB:
  def __init__(self):
    self.data = {}  # Main data store
    self.txn_data = {}  # Temporary data store for transactions
    self.is_in_txn = False  # Flag to track ongoing transaction

  def get(self, key):
    """
    Retrieves the value associated with the key.
    Args:
        key (str): The key to retrieve the value for.
    Returns:
        int: The value associated with the key, or None if it doesn't exist.
    """
    return self.txn_data.get(key, self.data.get(key))

  def put(self, key, val):
    """
    Inserts or updates a key-value pair.
    Args:
        key (str): The key to insert or update.
        val (int): The value to associate with the key.
    Raises:
        Exception: If called outside of a transaction.
    """
    if not self.is_in_txn:
      raise Exception("Cannot put outside of a transaction")
    self.txn_data[key] = val

  def begin_transaction(self):
    """
    Starts a new transaction.
    """
    if self.is_in_txn:
      raise Exception("Cannot begin a new transaction while one is ongoing")
    self.txn_data = {}  # Clear temporary data for new transaction
    self.is_in_txn = True

  def commit(self):
    """
    Applies changes made within the transaction to the main data store.
    """
    if not self.is_in_txn:
      raise Exception("Cannot commit outside of a transaction")
    self.data.update(self.txn_data)
    self.txn_data = {}  # Clear temporary data after commit
    self.is_in_txn = False

  def rollback(self):
    """
    Aborts all changes made within the transaction.
    """
    if not self.is_in_txn:
      raise Exception("Cannot rollback outside of a transaction")
    self.txn_data = {}  # Discard temporary data on rollback
    self.is_in_txn = False

# Example usage
inmemoryDB = InMemoryDB()

# Should return None
print(inmemoryDB.get("A"))

# Throws an error
try:
  inmemoryDB.put("A", 5)
except Exception as e:
  print(e)

# Begin transaction
inmemoryDB.begin_transaction()

# Set A's value to 5
inmemoryDB.put("A", 5)

# Should return None (not committed yet)
print(inmemoryDB.get("A"))

# Update A's value to 6
inmemoryDB.put("A", 6)

# Commit the transaction
inmemoryDB.commit()

# Should return 6 (committed value)
print(inmemoryDB.get("A"))

# Throws an error (no open transaction)
try:
  inmemoryDB.commit()
except Exception as e:
  print(e)

# Throws an error (no ongoing transaction)
try:
  inmemoryDB.rollback()
except Exception as e:
  print(e)

# Should return None
print(inmemoryDB.get("B"))

# Begin transaction
inmemoryDB.begin_transaction()

# Set B's value to 10
inmemoryDB.put("B", 10)

# Rollback the transaction
inmemoryDB.rollback()

# Should return None (changes rolled back)
print(inmemoryDB.get("B"))
