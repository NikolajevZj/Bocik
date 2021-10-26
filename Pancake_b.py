import time
from web3 import Web3

PancakeABI = [{
        "inputs": [{
                "internalType": "uint256",
                "name": "amountOutMin",
                "type": "uint256"
            }, {
                "internalType": "address[]",
                "name": "path",
                "type": "address[]"
            }, {
                "internalType": "address",
                "name": "to",
                "type": "address"
            }, {
                "internalType": "uint256",
                "name": "deadline",
                "type": "uint256"
            }
        ],
        "name": "swapExactETHForTokens",
        "outputs": [{
                "internalType": "uint256[]",
                "name": "amounts",
                "type": "uint256[]"
            }
        ],
        "stateMutability": "payable",
        "type": "function"
}]

def trans(hash,klucz,swapowane_bnp,adrespublicznyportfela):
    bsc = "https://bsc-dataseed.binance.org/"
    web3 = Web3(Web3.HTTPProvider(bsc))
    print(web3.isConnected())

    # My own address to swap from
    sender_address = adrespublicznyportfela

    # This is global Pancake V2 Swap router address
    router_address = "0x10ED43C718714eb63d5aA57B78B54704E256024E"

    # always spend using Wrapped BNB
    spend = web3.toChecksumAddress("0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c")


    # Print out your balances just for checking
    balance = web3.eth.get_balance(sender_address)
    print(balance)

    humanReadable = web3.fromWei(balance, 'ether')
    print(humanReadable)

    # Contract id is the new token we are swaping to
    contract_id = web3.toChecksumAddress(hash)

    # Setup the PancakeSwap contract
    contract = web3.eth.contract(address=router_address, abi=PancakeABI)

    nonce = web3.eth.get_transaction_count(sender_address)

    start = time.time()
    print(web3.toWei('0.02', 'ether'))

    pancakeswap2_txn = contract.functions.swapExactETHForTokens(
        0,
        # here setup the minimum destination token you want to have, you can do some math, or you can put a 0 if you don't want to care
        [spend, contract_id],
        sender_address,
        (int(time.time()) + 1000000)
    ).buildTransaction({
        'from': sender_address,
        'value': web3.toWei(swapowane_bnp, 'ether'),  # This is the Token(BNB) amount you want to Swap from
        'gas': 250000,
        'gasPrice': web3.toWei('5', 'gwei'),
        'nonce': nonce,
    })

    signed_txn = web3.eth.account.sign_transaction(pancakeswap2_txn, private_key=klucz)
    tx_token = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    print(web3.toHex(tx_token))