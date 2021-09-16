from web3 import Web3
import subprocess
import requests
import argparse


def claimGems(kind, salt, address, private_key):
    try:
        transaction = gem_contract.functions.mine(kind, salt).buildTransaction(
            {'from': address,
             'gas': 300000,
             'nonce': w3.eth.get_transaction_count(address)})
        # transaction['gasPrice'] = Gas Price (comment this line for auto setting)
        signed_txn = w3.eth.account.sign_transaction(transaction,
                                                     private_key=private_key)

        txn_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        print('hash:', txn_hash)
        _ = w3.eth.wait_for_transaction_receipt(txn_hash)
        print("!!! TX DONE !!!")
        return True
    except:
        print("TX FAILED")
        return False


parser = argparse.ArgumentParser("Get the args")
parser.add_argument("--publicKey", type=str, required=True,
                    help="Your address/public key")

parser.add_argument("--privateKey", type=str, required=True,
                    help="Your private key")

parser.add_argument("--target_gem", type=int, required=True,
                    help="Gem kind: 0 = Turquoise | 1 = Pearl etc...")

parser.add_argument("--diff", type=int, required=False,
                    help="Difficulty")

parser.add_argument("--lineToken", type=str, required=True,
                    help="lineToken")

args = parser.parse_args()

target_gem = args.target_gem  # 0 = Turquoise | 1 = Pearl etc...
my_address = args.publicKey
private_key = args.privateKey
diff = args.diff

NOTIFY_AUTH_TOKEN = args.lineToken
notify_url = 'https://notify-api.line.me/api/notify'
notify_headers = {'Authorization': 'Bearer ' + NOTIFY_AUTH_TOKEN}

w3 = Web3(Web3.HTTPProvider("https://rpc.ftm.tools/"))
gem_addr = "0x342EbF0A5ceC4404CcFF73a40f9c30288Fc72611"  # fantom gem
gem_abi = """[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"kind","type":"uint256"}],"name":"Create","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"miner","type":"address"},{"indexed":true,"internalType":"uint256","name":"kind","type":"uint256"}],"name":"Mine","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256[]","name":"ids","type":"uint256[]"},{"indexed":false,"internalType":"uint256[]","name":"values","type":"uint256[]"}],"name":"TransferBatch","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"id","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"TransferSingle","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"string","name":"value","type":"string"},{"indexed":true,"internalType":"uint256","name":"id","type":"uint256"}],"name":"URI","type":"event"},{"inputs":[{"internalType":"uint256[]","name":"kinds","type":"uint256[]"}],"name":"acceptManager","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"id","type":"uint256"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address[]","name":"accounts","type":"address[]"},{"internalType":"uint256[]","name":"ids","type":"uint256[]"}],"name":"balanceOfBatch","outputs":[{"internalType":"uint256[]","name":"","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"kind","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"address","name":"to","type":"address"}],"name":"craft","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"name","type":"string"},{"internalType":"string","name":"color","type":"string"},{"internalType":"uint256","name":"difficulty","type":"uint256"},{"internalType":"uint256","name":"gemsPerMine","type":"uint256"},{"internalType":"uint256","name":"multiplier","type":"uint256"},{"internalType":"address","name":"crafter","type":"address"},{"internalType":"address","name":"manager","type":"address"}],"name":"create","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"exists","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"gemCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"gems","outputs":[{"internalType":"string","name":"name","type":"string"},{"internalType":"string","name":"color","type":"string"},{"internalType":"bytes32","name":"entropy","type":"bytes32"},{"internalType":"uint256","name":"difficulty","type":"uint256"},{"internalType":"uint256","name":"gemsPerMine","type":"uint256"},{"internalType":"uint256","name":"multiplier","type":"uint256"},{"internalType":"address","name":"crafter","type":"address"},{"internalType":"address","name":"manager","type":"address"},{"internalType":"address","name":"pendingManager","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"_maxGemCount","type":"uint256"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"kind","type":"uint256"},{"internalType":"uint256","name":"salt","type":"uint256"}],"name":"luck","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxGemCount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"kind","type":"uint256"},{"internalType":"uint256","name":"salt","type":"uint256"}],"name":"mine","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nonce","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"kinds","type":"uint256[]"}],"name":"renounceManager","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256[]","name":"ids","type":"uint256[]"},{"internalType":"uint256[]","name":"amounts","type":"uint256[]"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"safeBatchTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"id","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_maxGemCount","type":"uint256"}],"name":"setMaxGemCount","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"id","type":"uint256"}],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"kinds","type":"uint256[]"},{"internalType":"address","name":"to","type":"address"}],"name":"transferManager","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_owner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256[]","name":"kinds","type":"uint256[]"},{"internalType":"address","name":"crafter","type":"address"}],"name":"updateCrafter","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"kind","type":"uint256"},{"internalType":"bytes32","name":"entropy","type":"bytes32"}],"name":"updateEntropy","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"kind","type":"uint256"},{"internalType":"string","name":"name","type":"string"},{"internalType":"string","name":"color","type":"string"}],"name":"updateGemInfo","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"kind","type":"uint256"},{"internalType":"uint256","name":"difficulty","type":"uint256"},{"internalType":"uint256","name":"multiplier","type":"uint256"},{"internalType":"uint256","name":"gemsPerMine","type":"uint256"}],"name":"updateMiningData","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"kind","type":"uint256"}],"name":"uri","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"}]"""
gem_contract = w3.eth.contract(address=gem_addr, abi=gem_abi)

while True:
    diff = gem_contract.functions.gems(target_gem).call()[3]
    nonce = gem_contract.functions.nonce(my_address).call()
    print("RARITYGEMS: START subprocess")
    print("RARITYGEMS: DIFF ->", diff)
    print("RARITYGEMS: NONCE ->", nonce)

    res = subprocess.check_output(
        ['./Salt_searching.exe',
         '-nonce', str(nonce),
         '-diff', str(diff),
         '-address', my_address,
         '-kind', str(target_gem)],
        universal_newlines=True,
        stderr=subprocess.STDOUT)

    print("submiting tx")

    salt_result = int(res.split(':')[-1].replace(" ", ""))

    if(claimGems(target_gem, salt_result, my_address, private_key)):
        if NOTIFY_AUTH_TOKEN != '':
            body = {'message': 'Gem found \n٩(＾◡＾)۶'
                    + '\nkind: ' + str(target_gem)
                    + '\nwallet: ' + my_address
                    + '\nnonce: ' + str(nonce)
                    + '\nsalt: ' + str(salt_result)
                    + '\nTransaction DONE'
                    }
            res = requests.post(notify_url, data=body, headers=notify_headers)
        print(nonce, 'claimed')
        break
    else:
        if NOTIFY_AUTH_TOKEN != '':
            body = {'message': 'Claim failed \n｡ﾟ( ﾟஇ▽இﾟ)ﾟ｡'
                    + '\nRestart'
                    }
            res = requests.post(notify_url, data=body, headers=notify_headers)
        print(nonce, 'unclaimed')
        break
