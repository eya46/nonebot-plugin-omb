from nonebot import require
from nonebot.plugin import PluginMetadata

require("nonebot_plugin_omb.patch_base")

supported_adapters = None


try:
    require("nonebot_plugin_alconna")
    from nonebot.plugin import inherit_supported_adapters

    require("nonebot_plugin_omb.patch_alconna")
    supported_adapters = inherit_supported_adapters("nonebot_plugin_alconna")
except RuntimeError:
    pass

__plugin_meta__ = PluginMetadata(
    name="Ohh My Bot",
    description="我的Bot我做主~",
    usage="无",
    type="library",
    homepage="https://github.com/eya46/nonebot-plugin-omb",
    supported_adapters=supported_adapters,
)
