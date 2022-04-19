# web3_py_simple_storage

https://www.youtube.com/watch?v=M576WGiDBdQ

ganache


# Brownie Installation
python -m pip install --user pipx
python -m pipx ensurepath
pipx install eth-brownie

# Brownie Commands
brownie --version
brownie init --force
brownie compile
brownie run scripts/deploy.py

### New brownie account
brownie accounts new freecodecamp-account
brownie accounts list

brownie networks list

Ejecutar desde la carpeta!!!
brownie run deploy.py --network=rinkeby
https://rinkeby.etherscan.io/tx/0x7eb7b9aa11e9a18cfd02968aca6ebf8d72455629664fd86ec93b5febb5c22846

brownie run read_value.py --network rinkeby

# Brownie console
brownie console