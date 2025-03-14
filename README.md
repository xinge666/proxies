# HTTP代理池服务

一个简单的HTTP代理池服务，可以自动获取、测试和维护可用的代理IP地址。代理数据存储在Redis中，并提供HTTP API接口获取可用代理。

## 功能特点

- 自动抓取免费代理源
- 定时测试代理可用性
- 支持自定义测试URL
- 基于Redis存储代理信息
- 提供RESTful API
- 支持自定义GitHub代理配置

## 系统要求

- Python 3.6+
- Redis
- 相关Python包依赖

## 安装

1. 克隆代理池项目：
```bash
git clone <repository_url>
cd proxy-pool
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 配置Redis连接信息（proxies/config/config.py）

## 配置说明

在 `proxies/config/config.py` 中配置以下参数：

- `TEST_URLS`：用于测试代理可用性的目标URL列表
- `PROXY_SOURCES_PROXY`：用于访问GitHub的HTTP代理配置
- Redis连接参数
- 其他自定义配置项

## 使用方法

1. 启动代理池服务：
```bash
python main.py
```

2. API接口说明：

- 获取代理池状态：
```
GET http://127.0.0.1:5000/count

返回示例：
{
    "all": 411015,      # 总代理数
    "bad": 157866,      # 不可用代理数
    "good": 881,        # 可用代理数
    "queue": 250556     # 待测试代理数
}
```

- 获取随机可用代理：
```
GET http://127.0.0.1:5000/get

返回示例：
{
    "proxy": "127.133.114.9:80"
}
```

## 项目结构

```
proxies/
├── main.py              # 主程序入口
├── core/
│   ├── fetcher.py      # 代理获取模块
│   ├── tester.py       # 代理测试模块
│   └── db.py           # 数据库操作模块
└── config/
    └── config.py       # 配置文件
```

## 自定义代理源

如需添加新的代理源，请在 `proxies/core/fetcher.py` 中实现相应的获取逻辑。

## 贡献指南

欢迎提交Issue和Pull Request来帮助改进项目。

## 许可证

[选择合适的开源许可证]