"""
    Name: blockchain_4.py
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


# ---------------------------- CREATE BLOCK -------------------------------- #
def create_block(
        prior_block_hash: str,
    prior_block_number: int,
    transaction_data: str
) -> tuple:
    """
    This function creates a new block using the prior block hash, 
    block number, transaction data, and block hash
    :param prior_block_hash: str   - The hash of the prior block 
    :param prior_block_number: int - The block number of the prior block
    :param transaction_data: str   - The transaction data for the new block
    :return: tuple - The new block containing prior block hash, block number,
    transaction data, and block hash            
    """
    # Calculate the new block number by incrementing the prior block number
    block_number = prior_block_number + 1

    # Generate a new block hash using the 'bit_hash' function with the
    # concatenation of prior block hash, block number, and transaction data
    block_hash = bit_hash((prior_block_hash, block_number, transaction_data))

    # Create a new block tuple containing prior block hash, block number,
    # transaction data, and the newly calculated block hash
    new_block = (prior_block_hash, block_number, transaction_data, block_hash)

    # Return the newly created block
    return new_block


def main():
    # Create genesis block using 'create_block' function with initial values
    # Prior block hash is set to "0" to represent the initial state
    # Numbering starts at -1 to represent initial state before the first block
    genesis_block = create_block(
        "0",    # Prior block hash
        -1,     # Prior block number
        "Wallet 1 paid 1 bitcoin to Wallet 2"  # Transaction data
    )

    # Print the details of the genesis block
    print("Genisys Block:")
    print(genesis_block)
    print()

    # Initialize the prior_block variable with the genesis block for the loop
    prior_block = genesis_block

    # Iterate through the loop to generate and display 3 additional blocks
    for i in range(3):
        print(f"Block {i + 1}:")
        # Extract prior block hash and block number from the prior_block tuple
        prior_block_hash = prior_block[3]
        prior_block_number = prior_block[1]

        # Extracted prior block hash and block number are used as inputs
        # Update the transaction data to represent a payment from
        # Wallet 1 to Wallet 2, with an incremented bitcoin amount
        next_block = create_block(
            prior_block_hash,
            prior_block_number,
            f"Wallet 1 paid {i + 2} bitcoin to Wallet 2"
        )

        # Print the details of the newly generated block
        print(next_block)
        print()

        # Update the prior_block variable for the next iteration
        prior_block = next_block


if __name__ == '__main__':
    main()

