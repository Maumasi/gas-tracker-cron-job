import requests
from src.constants import BASE_FEE, ESTIMATED_GAS_PRICE, MAX_GAS_PRICE
from env import CONFIG
from editable_options import OPTIONS
from src.app.models.SlackModel import SlackBot


class GasTrackerAPI:
    __slack_bot: SlackBot
    
    def __init__(self):
        self.__slack_bot = SlackBot()
    
    
    def getLatestGasEstimates(self):
        url = f'https://{ CONFIG["BASE_URL"] }/gasprices/blockprices'    
        response_raw = requests.get(url, headers={ 'Authorization': CONFIG['KEY'] })
        response_dict = response_raw.json()
        self.__send_notifications(response_dict)
        
        
    def __send_notifications(self, gas_fee_responce):
        if(not isinstance(gas_fee_responce, dict) or ('blockPrices' not in gas_fee_responce)):
            return False
        
        gas_data = gas_fee_responce['blockPrices'][0]

        # default to base fee
        threshhold = OPTIONS['BASE_FEE']
        fee = float(gas_data['baseFeePerGas'])
        base_price = float(gas_data['baseFeePerGas'])
        
        if(OPTIONS['THRESHHOLD_TO_USE'] == ESTIMATED_GAS_PRICE): 
            threshhold = OPTIONS['ESTIMATED_GAS_PRICE']
            for gas_estimate in gas_data['estimatedPrices']:
                if(gas_estimate['confidence'] == 99): 
                    fee = gas_estimate['price']
                    break
            
        elif(OPTIONS['THRESHHOLD_TO_USE'] == MAX_GAS_PRICE): 
            threshhold = OPTIONS['MAX_GAS_PRICE']
            for gas_estimate in gas_data['estimatedPrices']:
                if(gas_estimate['confidence'] == 99): 
                    fee = gas_estimate['maxFeePerGas']
                    break
        
        if(fee and threshhold and (fee < threshhold)):
            estimate_str = ''
            for estimate in gas_data['estimatedPrices']:
                estimate_str += f"Conf: { estimate['confidence'] }% | Price: ${ estimate['price'] }\n"
            
            msg = f'''==:: <{OPTIONS['SLACK_USERNAME_TO_NOTIFY']}> Gas Price ::==\n\n'''
            msg += "*Base Price ${:.2f}*\n".format(base_price) 
            msg += '----------------\n'
            msg += estimate_str
            
            # send a notification to slack
            self.__slack_bot.postMsgSlack(msg)




