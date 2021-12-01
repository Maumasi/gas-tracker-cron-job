from typing import Dict
import requests
from datetime import datetime

class SlackBot():
    __postDict: Dict
    
    def __init__(self, *args):
        self.__postDict = {
            'url': 'https://hooks.slack.com/services/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',
            'headers': { 'Content-type': 'application/json' },
            'data': ''
        }
    
    
    def postMsgSlack(self, msg: str):
        self.__postDict['data'] = '{"text": "<@maumasi>\n'+ msg +'" }'
        response = requests.post(**self.__postDict)
        return response