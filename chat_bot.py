import requests
from werobot import WeRoBot
from tencent_ai import*
from baidu_ai import*

# def get_content(plus_item):
#     # 聊天的API地址
#     url = "https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat"
#     # 获取请求参数
#     plus_item = plus_item.encode('utf-8')
#     payload = md5sign.get_params(plus_item)
#     # r = requests.get(url,params=payload)
#     r = requests.post(url,data=payload)
#     return r.json()["data"]["answer"]

robot = WeRoBot(enable_session=False,
        token = 'wechat',
        APP_ID = 'wxd2037f04aeb582fb',
        APP_SECRET = 'ti8e627JwSwqSVYoPDH2E6qR1GqP65cGRNqpKimdGEf')
 
@robot.text
def hello(message):   
    rep= get_content(message.content)
    return rep


# 让服务器监听在 0.0.0.0:80
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()