"""
    Name: blockchain_4.py
    Author: 
    Created: 02/10/2024
    Purpose: Demonstrate how blockchain works in Python
"""
# Python hashing library
import hashlib


# ---------------------------- BIT HASH ----------------------------------- #
def bit_hash(data):

    # Convert the input data to a string
    string_data = str(data)

    # Encode the string data into bytes using UTF-8
    formatted_data = string_data.encode('utf-8')

    # Compute the SHA-256 hash of the formatted data
    # Convert it to a hexadecimal representation
    bit_hash = hashlib.sha256(formatted_data).hexdigest()

    # Return the resulting hexadecimal hash
    return bit_hash


# --------------------------- CREATE BLOCK -------------------------------- #
def create_block(prior_block_hash, prior_block_number, transaction_data):
    """ function named 'create_block' with parameters for prior block hash,
     prior block number, and transaction data    
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


# Create genesis block using the 'create_block' function with initial values
# Mumbering starts at 0
genesis_block = create_block(0, -1, "Wallet 1 paid 1 bitcoin to Wallet 2")

# Print the details of the genesis block
print("Genisys Block:")
print(genesis_block)
print()

# Initialize the prior_block variable with the genesis block for the loop
prior_block = genesis_block

# Iterate through the loop to generate and print 3 additional blocks
for i in range(3):
    print(f"Block {i + 1}:")
    # Extract prior block hash and block number from the prior_block tuple
    prior_block_hash = prior_block[3]
    prior_block_number = prior_block[1]

    # Extracted prior block hash and block number are used as inputs
    # Update the transaction data to represent a payment from
    # Wallet 1 to Wallet 2, with an incremented bitcoin amount
    next_block = create_block(
        prior_block_hash, prior_block_number, "Wallet 1 paid " +
        str(i + 2) + " bitcoin to Wallet 2"
    )

    # Print the details of the newly generated block
    print(next_block)
    print()
    # Update the prior_block variable for the next iteration
    prior_block = next_block
