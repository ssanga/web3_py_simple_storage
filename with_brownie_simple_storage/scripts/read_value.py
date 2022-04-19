from brownie import SimpleStorage, accounts, config
# brownie run read_value.py --network rinkeby

def read_contract():
    # print(SimpleStorage)
    # Es un array con los distintos despliegues
    # print(SimpleStorage[0])

    # Last deployment
    simple_storage = SimpleStorage[-1]
    print(simple_storage.retrieve())

def main():
    read_contract()

    