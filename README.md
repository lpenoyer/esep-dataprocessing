# In-Memory Key-Value Database with Transaction Support

This Python program implements an in-memory key-value database with transaction support as described in the provided assignment.

## Functionality

The database supports the following functions:

- `get(key)`: Retrieves the value associated with the given key.
- `put(key, val)`: Sets the value for the specified key. If a transaction is in progress, the changes are cached until committed.
- `begin_transaction()`: Starts a new transaction.
- `commit()`: Applies changes made within the transaction to the main state.
- `rollback()`: Reverts changes made within the transaction.

## Running the Code

To run the code, simply execute the `InMemoryDB.py` file using a Python interpreter. Ensure that you have Python installed on your system.

Example:

```bash
python InMemoryDB.py
```

## Modification for Future Assignments
To make this assignment an "official" assignment in the future, consider the following modifications:
- Provide more extensive unit tests to ensure robustness and correctness.
- Implement additional features such as support for nested transactions or concurrency control mechanisms.
- Enhance error handling and provide more informative error messages.
- Include documentation comments (docstrings) for all methods to facilitate understanding and maintainability.

This project is for ESEP Data Processing and Storage Assignment. 
