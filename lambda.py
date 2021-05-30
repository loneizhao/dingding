
import json
from botocore.vendored import requests

def lambda_handler(event,context): # text type
    url="https://oapi.dingtalk.com/robot/send?access_token=79fbe7044854f8bb407097457abf3e6a3f9da168558c8381a08ada1f1bcd4c96"
    message = event['Records'][0]['Sns']
    Timestamp=message['Timestamp']
    Subject=message['Subject']
    pagrem={
    "msgtype":"markdown",
        "markdown": {"title":"AWS Alert",
             "text":"## "+Subject+"\n ### beijing:"+Timestamp+" \n ### 内容："+Subject+" \n"
        },
        "at":{
            "atMobiles":[
                "185xxxxxxxx"
            ]
    },
        "isAtAll": "true"
    }
    headers={
        'Content-Type':'application/json'
    }
    requests.post(url,data=json.dumps(pagrem),headers=headers)
