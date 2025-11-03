import os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

RPC_URL = os.getenv("BASE_RPC_URL")
if not RPC_URL:
    raise SystemExit("Установите переменную окружения BASE_RPC_URL")

w3 = Web3(Web3.HTTPProvider(RPC_URL))

if not w3.is_connected():
    raise SystemExit("Не удалось подключиться к RPC.")

chain_id = w3.eth.chain_id
latest = w3.eth.get_block('latest')

print(f"Connected to RPC: {RPC_URL}")
print(f"chainId: {chain_id}")
print(f"latest block number: {latest.number}")
