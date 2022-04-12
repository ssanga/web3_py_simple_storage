# web3_py_simple_storage

https://www.youtube.com/watch?v=M576WGiDBdQ

ganache


# Brownie Installation
python -m pip install --user pipx
python -m pipx ensurepath

pipx install eth-brownie

brownie --version
brownie init --force
brownie compile
brownie run scripts/deploy.py

### New brownie account
brownie accounts new freecodecamp-account
brownie accounts list