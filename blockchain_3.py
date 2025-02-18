"""
    Name: blockchain_3.py
    Author: 
    Created: 02/10/2024
    Purpose: Demonstrate how blockchain works in Python
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

    # Create the transaction for block 2
    transaction_2 = "Wallet 1 paid 2 bitcoin to Wallet 2"

    # Create the block 2 hash which combines the previous hash
    block_2_hash = bit_hash((genesis_block_hash, transaction_2))

    # The block now holds all the transactions details and hash chains
    block_2 = (genesis_block_hash, transaction_2, block_2_hash)

    print(block_2)


if __name__ == '__main__':
    main()
