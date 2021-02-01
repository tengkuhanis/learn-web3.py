from web3 import Web3

# Fill in your infura API key here
infura_url = "https://mainnet.infura.io/v3/8cdf50bef35e401da664c4af39116ef1"
web3 = Web3(Web3.HTTPProvider(infura_url))
'''
# get latest block number
latest = web3.eth.blockNumber
print(latest)
# get latest block
print(web3.eth.getBlock(latest))

# get latest 10 blocks
for i in range(0, 10):
  print(web3.eth.getBlock(latest - i))
'''
# get transaction from specific block
hash = '0xa2e0087cea2d42c790d0f3f761fce096de70f4c73e58ddb216d122f601167ae9'
print(web3.eth.getTransactionByBlock(hash, 3))
