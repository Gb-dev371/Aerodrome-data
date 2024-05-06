from web3_scan_api.scan_api import ScanApi
from web3_scan_api.utils.functions import timestamp_to_date


def get_bribes_created(scan_api:ScanApi, pool_contract_address, bribe_contract_address, voter_contract_address='0x16613524e02ad97eDfeF371bC883F2F5d6C480A5'):
    bribe_contracts_list = []
    voter_contract_abi = scan_api.get_contract_abi(voter_contract_address)
    voter_contract = scan_api.get_contract(voter_contract_address, voter_contract_abi)

    gauge_address = voter_contract.functions.gauges(pool_contract_address).call()
    bribe_contract_address = voter_contract.functions.gaugeToBribe
    for tx in scan_api.get_transactions(bribe_contract_address):
        
        if (tx['to']).lower() == bribe_contract_address.lower():
            
            if tx['functionName'] == 'notifyRewardAmount(address _rewardsToken, uint256 reward)':
                
                block_number = int(tx['blockNumber'])
                input_data = tx['input']
                input_decoded = scan_api.get_input_decoded(bribe_contract_address, input_data)[1] # {'token': '0xA3d1a8DEB97B111454B294E2324EfAD13a9d8396', 'amount': 250000000000000000000}
                
                
                tx_hash = tx['hash']
                timestamp = scan_api.get_timestamp(tx_hash)
                date = timestamp_to_date(timestamp)
                input_decoded['Tx hash'] = tx_hash
                input_decoded['Timestamp'] = timestamp
                input_decoded['Block Number'] = block_number
                input_decoded['Date'] = date
                bribe_contracts_list.append(input_decoded)
            
    return bribe_contracts_list
