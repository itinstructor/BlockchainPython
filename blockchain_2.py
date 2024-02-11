"""
    Name: blockchain_2.py
    Author: 
    Created: 02/10/2024
    Purpose: Demonstrate blockchain in Python
"""
# Python hashing library
import hashlib


# --------------------------- BIT HASH ------------------------------------ #
def bit_hash(data):

    # Convert the input data to a string
    string_data = str(data)

    # Encode the string data into bytes using UTF-8 text encoding
    formatted_data = string_data.encode('utf-8')

    # Compute the SHA-256 hash of the formatted data
    bit_hash = hashlib.sha256(formatted_data)

    # Convert it to a hexadecimal representation
    bit_hash = bit_hash.hexdigest()

    # Return the resulting hexadecimal hash
    return bit_hash


# Start with a basic block
# Define a transaction where Wallet 1 pays 1 bitcoin to Wallet 2
transaction_1 = "Wallet 1 paid 1 bitcoin to Wallet 2"

# Create a genesis block hash containing the transaction hash
genesis_block_hash = bit_hash((0, transaction_1))

# Print the contents of the genesis block
print(genesis_block_hash)

# Recreate the genesis block - this time with hashes for our chain
genesis_block = (0, transaction_1, genesis_block_hash)

# Print the complete genisis block
print(genesis_block)


