"""
    Name: blockchain_2.py
    Author: 
    Created: 02/10/2024
    Purpose: Demonstrate blockchain in Python
"""
# Python hashing library
import hashlib


# ---------------------------- BIT HASH ------------------------------------ #
def bit_hash(data: tuple) -> str:
    """
    This function takes a tuple of data 
    and returns a SHA-256 hash in hexadecimal
    :param data: tuple
    :return: str
    """
    # Convert the input data tuple to a string
    string_data = str(data)

    # Encode string data into bytes using UTF-8 text encoding
    byte_data = string_data.encode('utf-8')

    # Compute the SHA-256 bit hash of the byte data
    bit_hash = hashlib.sha256(byte_data)

    # Convert it to a hexadecimal string representation
    bit_hash_hex = bit_hash.hexdigest()

    # Return the resulting hexadecimal string
    return bit_hash_hex


def main():
    # Start with a basic block
    # Define a transaction where Wallet 1 pays 1 bitcoin to Wallet 2
    transaction_1 = "Wallet 1 paid 1 bitcoin to Wallet 2"

    # Create a genesis block hash containing the transaction hash
    genesis_block_hash = bit_hash((0, transaction_1))

    # Recreate the genesis block - this time with hashes for our chain
    genesis_block = (0, transaction_1, genesis_block_hash)

    # Print the complete genisis block
    print(genesis_block)


if __name__ == '__main__':
    main()


