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

通过patch `on_command` 和 `on_alconna`, 注入 `SuperUserRule`

- patch `on_command` 使 `bot` 只响应 `SuperUser` 的命令

> 从 `nonebot.plugin.on import on_command` 导入的没法patch, 请使用 `nonebot.on_command` 导入

- patch `on_alconna` 使 `bot` 只响应 `SuperUser` 的消息


## 安装方式

### 依赖管理

- `pip install nonebot-plugin-omb`
- `poetry add nonebot-plugin-omb`
- `pdm add nonebot-plugin-omb`

> 在 `bot.py` 中添加 `nonebot.load_plugin("nonebot_plugin_omb")`


**⚠️ 请确保 `nonebot_plugin_omb` 加载优先级高于其他插件**

## 配置项

### 必要配置项

```env
# 在 nonebot-plugin-alconna>=0.53.0 版本中, 推荐配置(响应Bot的消息)
ALCONNA_RESPONSE_SELF=True

# 记得配置 SUPERUSERS
SUPERUSERS=["xxxxxx"]
```

## 依赖项

```toml
python = "^3.9"
nonebot2 = "^2.3.0"
nonebot-plugin-alconna = { version = ">=0.53.0", optional = true }
```
