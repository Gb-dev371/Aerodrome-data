from web3_scan_api.scan_api import ScanApi
from dotenv import load_dotenv
from web3_scan_api.info import base, API_KEY_BASE_SCAN
import os 
from web3 import Web3 
from aerodrome.bribes import get_bribes_created

load_dotenv(override=True)
API_KEY_BINANCE_SCAN = os.getenv('BINANCE_SCAN_API_KEY')
API_KEY_POLYGON_SCAN = os.getenv('POLYGON_SCAN_API_KEY')
API_KEY_INFURA = os.getenv('INFURA_API_KEY')


pol = Web3(Web3.HTTPProvider(f'https://polygon-mainnet.infura.io/v3/{API_KEY_INFURA}'))
polygon_scan = ScanApi(rpc=pol, chain='MATIC', api_key=API_KEY_POLYGON_SCAN)
base_scan = ScanApi(rpc=base, chain='BASE', api_key=API_KEY_BASE_SCAN)

native_token_balance_polygon = polygon_scan.get_native_token_balance(account_address='0x3829cD969b481E32b77b32Bb7F41cD56BD95680A')
native_token_balance_base = base_scan.get_native_token_balance(account_address='0x3829cD969b481E32b77b32Bb7F41cD56BD95680A')
# print(native_token_balance_polygon)
# print(native_token_balance_base)

bribes_contract_list = get_bribes_created(base_scan, '0x9e9278867c250d003d27a025e272e62ff824ef22')
for bribe in bribes_contract_list:
    print(bribe)