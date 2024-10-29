from nonebot import Bot, require
from nonebot.plugin import PluginMetadata
from nonebot.message import event_preprocessor
from nonebot.exception import IgnoredException
from nonebot.internal.adapter import Event

from .util import SuperUserObj

require("nonebot_plugin_omb.patch_base")

supported_adapters = None


@event_preprocessor
def only_me_check(bot: Bot, event: Event):
    if not SuperUserObj(bot, event):
        raise IgnoredException("only superuser!")


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
