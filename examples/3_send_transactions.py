from web3 import Web3

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

print(web3.isConnected())
print(web3.eth.blockNumber)

account_3 = '0xdC6ACb7C29C7AA5648b66b641ddEcF8d045737dE' # Fill me in
account_4 = '0xe190B3A85294E7bba9314Ffaa47B0C8D2586D245' # Fill me in
private_key = 'a86cfc43cff5f63025f0b89b3ed95faffb9903323045c8373e0ce5b8f3a1543a' #pk of sending acc # Fill me in

#get nonce
nonce = web3.eth.getTransactionCount(account_4) # this prevents double-spend problem

#build transaction
tx = {
    'nonce': nonce,
    'to': account_3,
    'value': web3.toWei(50, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei'),
}

#sign transaction
signed_tx = web3.eth.account.signTransaction(tx, private_key)

#send transaction
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

#get transaction
print(tx_hash) # tx hash presented in a complex way
print(web3.toHex(tx_hash)) # tx hash presented in hexadecimal
