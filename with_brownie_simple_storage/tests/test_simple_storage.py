# Execute as VSCODE AS ADMIN!!!!!!
# brownie test -s

# Para solo ejecutar un test:
# brownie test -k test_updating_storage
from brownie import SimpleStorage, accounts

def test_deploy():
    # Arrage
    account = accounts[0]
    # Act
    simple_storage = SimpleStorage.deploy({'from': account})
    starting_value = simple_storage.retrieve()
    expected_value = 0
    # Assert
    assert starting_value == expected_value

def test_updating_storage():
    # Arrage
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({'from': account})
    # Act
    expected_value = 15
    simple_storage.store(expected_value, {'from': account})
    updated_value = simple_storage.retrieve()
    # Assert
    assert updated_value == expected_value

