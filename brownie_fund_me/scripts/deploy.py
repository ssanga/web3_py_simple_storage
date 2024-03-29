from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import get_account

# brownie run scripts/deploy.py --network rinkeby

# Para pruebas
# brownie run scripts/deploy.py 


def deploy_fund_me():
    account = get_account()
    # pass the price feed address to our fundme contract

    # if we are on a persistent network like rinkeby, use the associated address
    # otherwise, deploy mocks
    if(network.show_active() != "development"):
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        print(f"The active network is {network.show_active()}")
        print(f"Deploying Mocks...")
        mock_aggregator =  MockV3Aggregator.deploy(18,200000000000000000000, {"from":account})
        price_feed_address = mock_aggregator.address
        print("Mocks Deployed")

    fund_me = FundMe.deploy(price_feed_address,
                            {"from": account}, 
                            publish_source=config["networks"][network.show_active()].get("verify"))
    print(f"Contract deployed at {fund_me.address}")



def main():
    deploy_fund_me()