<p align="center">
  <a href="https://nonebot.dev/"><img src="https://nonebot.dev/logo.png" width="200" height="200" alt="nonebot"></a>
</p>

<div align="center">

# NoneBot Plugin OMB

# Ohh My Bot!

![License](https://img.shields.io/github/license/eya46/nonebot-plugin-omb)
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![NoneBot](https://img.shields.io/badge/nonebot-2.3.0+-red.svg)
</div>

## 作用

在 `onebot v11` 和 `nonebot-plugin-alconna` 只响应 `SUPERUSER` 的消息

## 安装方式

### 依赖管理

- `pip install nonebot-plugin-omb`
- `poetry add nonebot-plugin-omb`
- `pdm add nonebot-plugin-omb`

> 在 `bot.py` 中添加 `nonebot.load_plugin("nonebot_plugin_omb")`

### nb-cli

- `nb plugin install nonebot-plugin-omb`

## 配置项

### 必要配置项

```env
# 在 nonebot-plugin-alconna>=0.53.0 版本中, 务必配置
ALCONNA_RESPONSE_SELF=True

# 记得配置 SUPERUSERS
# 仅测试下面这种配置方式
SUPERUSERS=["xxxxxx"]
```

## 依赖项

```toml
python = "^3.9"
nonebot2 = "^2.3.0"
nonebot-adapter-onebot = "^2.1.0"
nonebot-plugin-alconna = { version = ">=0.53.0", optional = true }
```
