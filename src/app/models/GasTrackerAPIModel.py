import os
import requests
from pathlib import Path
import pandas as pd
from datetime import datetime
from pprint import pprint
from env import CONFIG
from src.app.models.SlackModel import SlackBot



class GasTrackerAPI:
    __slack_bot: SlackBot
    
    def __init__(self):
        self.__slack_bot = SlackBot()
    
    
    def getLatestGasEstimates(self):
        url = f'https://{ CONFIG["BASE_URL"] }/gasprices/blockprices'
        parameters = {
            # 'start':'1',
            # 'sort':'date_added',
            # 'sort_dir': 'desc' ,
            # 'limit': 400,
        }

        headers = {
            'Authorization': CONFIG['KEY'],
        }
    
        response_raw = requests.get(url, params=parameters, headers=headers)
        response_dict = response_raw.json()
        self.__send_notifications(response_dict)
        
        
    def __send_notifications(self, gas_fee_responce):
        if(not isinstance(gas_fee_responce, dict) or ('blockPrices' not in gas_fee_responce)):
            return False
        
        gas_data = gas_fee_responce['blockPrices'][0]
        base_fee = float(gas_data['baseFeePerGas'])

        
        if(base_fee < 80):
            estimate_str = ''
            for estimate in gas_data['estimatedPrices']:
                estimate_str += f"Conf: { estimate['confidence'] }% | Price: ${ estimate['price'] }\n"
            
            msg = '==:: Gas Price ::==\n\n'
            msg += "*Base Price ${:.2f}*\n".format(base_fee) 
            msg += '----------------\n'
            msg += estimate_str
            
            # send a notification to slack
            self.__slack_bot.postMsgSlack(msg)




