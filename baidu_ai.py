# -*- coding: utf-8 -*-
from aip import AipNlp
# from twilio.rest import Client

def is_pessimistic(text):
    #SDK的方式，腾讯的是API的方式

  #################在这里更改自己的信息#######################
    """ 你的 APPID AK SK """
    APP_ID = ''
    API_KEY = ''
    SECRET_KEY = ''
  #################在这里更改自己的信息#######################

    client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

    


    """ 如果有可选参数 """
    options = {}
    options["scene"] = "talk"

    """ 带参数调用对话情绪识别接口 """
    result = client.emotion(text, options)
    result_items = result["items"]
    for lab_dic in result_items:
        if lab_dic["prob"] > 0.5:
            label = lab_dic["label"]
        break

    if label == "pessimistic":
        return True
    else:
        return False