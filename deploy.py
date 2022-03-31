# pip install py-solc-x
# pip install web3

import json
from solcx import compile_standard, install_solc
from web3 import Web3

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



url = "http://127.0.0.1:7545"
# for connecting to local blockchain ganache
w3 = Web3(Web3.HTTPProvider(url))
chain_id = 5777
my_address ="0x3Faf7016b314F8F50e6d69A95Fabf690eBE3DeA4"
private_key = "0x9db43dca2a9d42682b3f8c2495ad2e5a9875d9345e7a46886db3cdce072b6f47"

SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
# print(SimpleStorage)
