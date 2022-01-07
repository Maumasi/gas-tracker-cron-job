from typing import Dict
import requests
from env import CONFIG


class SlackBot():
    __postDict: Dict

    def __init__(self, *args):
        self.__postDict = {
            'url': CONFIG['SLACK']['CHANNEL_WEBHOOK'],
            'headers': {
                'Content-type': 'application/json',
                # 'Authorization:': f"Bearer {CONFIG['SLACK']['KEY']}",
            },
            'data': ''
        }


    def postMsgSlack(self, msg: str):
        self.__postDict['data'] = '{"text": "'+ msg +'" }'
        response = requests.post(**self.__postDict)
        return response