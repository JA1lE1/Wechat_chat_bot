# AI入门级解决方案 :see_no_evil:

![image title](https://img.shields.io/badge/auther-JA1LE1-orange.svg)![image title](https://img.shields.io/badge/XMU-CSC-blue.svg)![image title](https://img.shields.io/badge/Ubuntu-passing-brightgreen.svg)

本方案介绍几种（当前1种）实现当前流行的人工智能应用场景的入门级解决方案 ,推荐运行环境：Ubuntu Server 16.04.1 LTS 64位

## 聊天机器人

#### 实现功能

---

- 智能闲聊
- 情绪分析

#### 安装依赖

```python
pip install -r requirement.txt
pip3 install -r requirement3.txt
```



#### 获取代码

```
git clone https://github.com/JA1lE1/wechat_bot.git
```



#### 前端实现方式:fire:

- 准备好:100:
  - 需有一个微信公众号，订阅号即可。
    - 并在微信公众平台的基本配置中查看开发者ID并记录，==便于在代码中修改为自己的==
    - 配置好服务器设置，并在==服务器chat_bot主程序== 运行后提交相关配置
  - 一台云服务器，这里推荐使用腾讯云服务器,腾讯云+校园10元/月的费用还是较为合适，当然如果你有谷歌云服务就更好了，省去了很多备案的步骤。



#### WeRoBot:fire:

- 本解决方案使用WeRoBot的微信公众号开发框架
  - [官方文档-CN](https://werobot.readthedocs.io/zh_CN/latest/index.html)
  - 由于只处理文本数据，这里只使用@robot.text这个handler,并让服务器监听在0.0.0.0:80
    - 监听在80端口是由于微信公众号的服务器地址只支持80端口
  - ==代码部分==

#### 腾讯AI平台的应用接入

- 步骤一，选择所需要的AI技术引擎
  - ![腾讯AI指引](E:\work\github\JA1lE1.github.io\My_Daily_Work\笔记\2019\3月\picture\腾讯AI指引.png)

- 步骤二，登录控制台
  - ![登录控制台](E:\work\github\JA1lE1.github.io\My_Daily_Work\笔记\2019\3月\picture\登录控制台.png)
- 创建自己的AI应用，并填写好相应内容
  - ![创建应用](E:\work\github\JA1lE1.github.io\My_Daily_Work\笔记\2019\3月\picture\创建应用.png)
- 选择免费使用某个AI引擎，并将其能力接入刚刚创建的应用之中
  - ![免费使用智能闲聊](E:\work\github\JA1lE1.github.io\My_Daily_Work\笔记\2019\3月\picture\免费使用智能闲聊.png)
  - ![接入能力](E:\work\github\JA1lE1.github.io\My_Daily_Work\笔记\2019\3月\picture\接入能力.png)
  - 在控制台的应用管理中选择自己刚刚创建的应用，进入后点击应用信息，记录自己的APPID 和APPKEY，或将其复制在某个文本中，以备在==代码.py== 中修改为自己APPID和APPKEY.
- 查看官方文档的智能闲聊部分可以发现只有PHP的tutorial，这里改用python实现同样的效果。
- ==代码==

#### 运行

```
python3 chat_bot.py
```



#### supervisord 启动命令

```
supervisord -c supervisor.conf
```









