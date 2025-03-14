# proxies

基于大佬们的http 代理文件，维护一个对自己项目可用的代理地址池 

数据存放在 redis 中
TEST_URLS： 自己的目标URL
PROXY_SOURCES_PROXY ： 自己用于访问 GitHub 的http 代理

python main.py 启动 falsk 服务


get http://127.0.0.1:5000/count 获取当前 ip 池状态
{"all":411015,"bad":157866,"good":881,"queue":250556}

get http://127.0.0.1:5000/get # 获取随机可用代理
{"proxy":"127.133.114.9:80"}