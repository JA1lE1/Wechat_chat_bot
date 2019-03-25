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
    if is_pessimistic(message.content):
        rep = "十分抱歉给您带来的不便，我们这边马上安排工作人员和您沟通。"
        # account_sid = "ACc290a6cb0258540264b0ebb1f6a37d60"
        # auth_token = "fa5c345aedc44bc5888f843a3bbe53ed"
        # client = Client(account_sid, auth_token)
        # message = client.messages.create(to="+8617359870570",  # 区号+你的手机号码
        #                                 from_="+12023359371",  # 你的 twilio 电话号码
        #                                 body="你的客户xxx，需要你马上处理。")
        return rep
    else:    
        rep= get_content(message.content)
        return rep


# 让服务器监听在 0.0.0.0:80
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()
