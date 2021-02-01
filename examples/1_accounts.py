from web3 import Web3

# Fill in your infura API key here
infura_url = "https://mainnet.infura.io/v3/8cdf50bef35e401da664c4af39116ef1"
web3 = Web3(Web3.HTTPProvider(infura_url))

print(web3.isConnected())

print(web3.eth.blockNumber)

# Fill in your account here
balance = web3.eth.getBalance("0x638352A2515aaECc6405A831E2d39153EA581172")
print(web3.fromWei(balance, "ether"))
