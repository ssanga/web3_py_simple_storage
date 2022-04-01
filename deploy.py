# pip install py-solc-x
# pip install web3

import json
from solcx import compile_standard, install_solc
from web3 import Web3
import os

with open("./SimpleStorage.sol", "r") as file:
    simple_storage_file = file.read()
    # print(simple_storage_file)

install_solc("0.6.0")

# Compile Our Solidity
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]}
            }
        }
    },
    solc_version="0.6.0"
)

# print(compiled_sol)
with open("compiled_code.json","w") as file:
    json.dump(compiled_sol, file)

# get bytecode
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]

# get abi
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]


# for connecting to local blockchain ganache
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chain_id = 5777
my_address ="0xA387114ECA42FE5bF6e7941ea474a4aB2539b32F"
# private_key = "0x11c5194b00bf683ec510f73ce164e74f7a03285fc99e53c97bcb8d059fd8e4d0"
private_key = os.getenv("PRIVATE_KEY")

# Create the contract in python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
print(SimpleStorage)

# Get the latest transaction
nonce = w3.eth.getTransactionCount(my_address)
print(nonce)

# 1. Build a transaction
transaction = SimpleStorage.constructor().buildTransaction(
    # {"chainId:": chain_id, "from": my_address, "nonce": nonce, "gasPrice": w3.eth.gas_price}
    {"from": my_address, "nonce": nonce, "gasPrice": w3.eth.gas_price}
)
# print(transaction)

# 2. Sign the transaction
signed_transaction = w3.eth.account.sign_transaction(transaction, private_key)
# print(signed_transaction)

# 3. Send the transaction
transation_hash = w3.eth.sendRawTransaction(signed_transaction.rawTransaction)
transaction_receipt = w3.eth.wait_for_transaction_receipt(transation_hash)

# Working with the contract
# Contract Address
# Contract ABI
simple_storage = w3.eth.contract(address=transaction_receipt.contractAddress, abi=abi)
# Call -> Simulate making the call and getting a return value
# Transact -> Actually make a state change

# Initial value of favorite number
print(simple_storage.functions.retrieve().call())
# print(simple_storage.functions.store(15).call())
store_transaction = simple_storage.functions.store(15).buildTransaction(
    {"from": my_address, "nonce": nonce + 1, "gasPrice": w3.eth.gas_price}
)

signed_store_tx = w3.eth.account.sign_transaction(store_transaction, private_key)
send_store_tx = w3.eth.sendRawTransaction(signed_store_tx.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(send_store_tx)
print(simple_storage.functions.retrieve().call())