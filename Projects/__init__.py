from flask import Flask, request, abort
import requests
import json
from Projects.Config import *
app = Flask(__name__)


def Get_covid():
    data = requests.get('https://covid19.th-stat.com/api/open/today/')
    Confirmed = data.json()['Confirmed']
    Recovered = data.json()['Recovered']
    Hospitalized = data.json()['Hospitalized']
    Deaths = data.json()['Deaths']
    NewConfirmed = data.json()['NewConfirmed']
    NewRecovered = data.json()['NewRecovered']
    NewHospitalized = data.json()['NewHospitalized']
    NewDeaths = data.json()['NewDeaths']
    UpdateDate = data.json()['UpdateDate']
    Source = data.json()['Source']
    
    text_mes = {
            "type": "flex",
            "altText": "Flex Message",
            "contents": {
            "type": "bubble",
            "body": {
            "type": "box",
            "layout": "vertical",
            "spacing": "md",
            "contents": [
                {
                "type": "text",
                "text": "TH - COVID 19",
                "size": "xxl",
                "weight": "bold",
                "color": "#FF0000"
                },
                {
                "type": "separator"
                },
                {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                    {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                        {
                        "type": "icon",
                        "url": "https://cdn.pixabay.com/photo/2020/04/29/07/54/coronavirus-5107715_1280.png"
                        },
                        {
                        "type": "text",
                        "text": "ติดเชื้อสะสม ",
                        "flex": 0,
                        "margin": "sm",
                        "weight": "bold"
                        },
                        {
                        "type": "text",
                        "text": str(Confirmed)+" (เพิ่มขึ้น "+str(NewConfirmed)+")",
                        "size": "sm",
                        "align": "end",
                        "color": "#AAAAAA"
                        }
                    ]
                    },
                    {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                        {
                        "type": "icon",
                        "url": "https://cdn.iconscout.com/icon/free/png-256/hospital-doctor-medicine-emergency-service-healthcare-emoj-symbol-30736.png"
                        },
                        {
                        "type": "text",
                        "text": "รักษาตัวอยู่ รพ",
                        "flex": 0,
                        "margin": "sm",
                        "align": "center",
                        "weight": "bold"
                        },
                        {
                        "type": "text",
                        "text": str(Hospitalized),
                        "size": "sm",
                        "align": "end",
                        "color": "#AAAAAA"
                        }
                    ]
                    },
                    {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                        {
                        "type": "icon",
                        "url": "https://image.flaticon.com/icons/png/512/564/564276.png"
                        },
                        {
                        "type": "text",
                        "text": "หายแล้ว ",
                        "flex": 0,
                        "margin": "sm",
                        "align": "center",
                        "weight": "bold"
                        },
                        {
                        "type": "text",
                        "text": str(Recovered) + " (เพิ่มขึ้น "+str(NewRecovered)+")",
                        "size": "sm",
                        "align": "end",
                        "color": "#AAAAAA"
                        }
                    ]
                    },
                    {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                        {
                        "type": "icon",
                        "url": "https://lh3.googleusercontent.com/proxy/Dje3mfTMaiMesS94wbSoOmJpBZFHFHX1lUnrts5530mk6GXI4VY3l8lxCBmdZ1m1kO4YrlN08EPDJ8lw7Gi2m1dP_D3Dc3dZt7kwFrzuNkL5G5pcP2zznJmC8Q"
                        },
                        {
                        "type": "text",
                        "text": "เสียชีวิต",
                        "flex": 0,
                        "margin": "sm",
                        "weight": "bold"
                        },
                        {
                        "type": "text",
                        "text": str(Deaths)+" (เพิ่มขึ้น "+str(NewDeaths)+")",
                        "size": "sm",
                        "align": "end",
                        "color": "#AAAAAA"
                        }
                    ]
                    },
                    {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                        {
                        "type": "icon",
                        "url": "https://static.thenounproject.com/png/113949-200.png"
                        },
                        {
                        "type": "text",
                        "text": "อัตราการเสียชีวิต",
                        "flex": 0,
                        "margin": "sm",
                        "weight": "bold"
                        },
                        {
                        "type": "text",
                        "text": str(round((Deaths*100)/Confirmed,2)),
                        "size": "sm",
                        "align": "end",
                        "color": "#AAAAAA"
                        }
                    ]
                    },
                    {
                    "type": "box",
                    "layout": "baseline",
                    "contents": [
                        {
                        "type": "icon",
                        "url": "https://image.flaticon.com/icons/png/512/314/314373.png"
                        },
                        {
                        "type": "text",
                        "text": "อัตราการหาย",
                        "flex": 0,
                        "margin": "sm",
                        "weight": "bold"
                        },
                        {
                        "type": "text",
                        "text": str(round((Recovered*100)/Confirmed,2)),
                        "size": "sm",
                        "align": "end",
                        "color": "#AAAAAA"
                        }
                    ]
                    },
                    {
                    "type": "separator"
                    }
                ]
                },
                {
                "type": "text",
                "text": "อัพเดตเมื่อ  : "+ str(UpdateDate),
                "size": "xxs",
                "color": "#AAAAAA",
                "wrap": True
                },
                {
                "type": "text",
                "text": "ข้อมูลโดย : "+str(Source),
                "size": "xxs",
                "color": "#AAAAAA",
                "wrap": True
                },
                {
                "type": "text",
                "text": "BOT BY FlyInSpace",
                "size": "xxs",
                "color": "#AAAAAA",
                "wrap": True
                }
                ]
                }
            }
        }
    return text_mes


@app.route('/webhook', methods=['POST','GET'])
def webhook():
    if request.method == 'POST':
        payload = request.json

        Reply_token = payload['events'][0]['replyToken']
        print(Reply_token)
        message = payload['events'][0]['message']['text']
        print(message)
        if "covid" in message:
            Reply_messasge = Get_covid()
            ReplyMessage(Reply_token,Reply_messasge,Channel_access_token)
        return request.json, 200

    elif request.method == 'GET' :
        return 'this is method GET!!!' , 200

    else:
        abort(400)

@app.route('/')
def hello():
    return 200

def ReplyMessage(Reply_token, TextMessage, Line_Acees_Token):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    Authorization = 'Bearer {}'.format(Line_Acees_Token) 
    print(Authorization)
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization':Authorization
    }

    data = {
        "replyToken":Reply_token,
        "messages":[TextMessage]
    }

    data = json.dumps(data) ## dump dict >> Json Object
    r = requests.post(LINE_API, headers=headers, data=data) 
    return 200