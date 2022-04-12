import os
from brownie import accounts, config, SimpleStorage

def deploy_simple_storage():
    account = accounts[0]
    print(account)
    
    # account = accounts.load("freecodecamp-account")
    # print(account)

    # account = accounts.add(os.getenv("PRIVATE_KEY_METAMASK"))
    # print(account)

    # account = accounts.add(config["wallets"]["from_key"])
    # print(account)

    simple_storage =  SimpleStorage.deploy({'from': account})
    # print(simple_storage)
    stored_value = simple_storage.retrieve()
    print(f"Stored Value: {stored_value}")
    transaction = simple_storage.store(15, {'from': account})
    transaction.wait(1)
    updated_value = simple_storage.retrieve()
    print(f"Stored Value: {updated_value}")

def main():
    deploy_simple_storage()