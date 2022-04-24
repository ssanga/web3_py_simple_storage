from brownie import FundMe, network
from scripts.helpful_scripts import get_account



def deploy_fund_me():
    account = get_account()
    fund_me = FundMe.deploy({"from": account})
    print(f"Contract deployed at {fund_me.address}")



def main():
    deploy_fund_me()