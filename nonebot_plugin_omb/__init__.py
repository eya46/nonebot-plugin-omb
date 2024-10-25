from nonebot import Bot, require
from nonebot.plugin import PluginMetadata
from nonebot.message import event_preprocessor
from nonebot.exception import IgnoredException
from nonebot.adapters.onebot.v11 import Bot as V11Bot

from .util import SUPERUSERS
from .patch_base import *

supported_adapters = set()


@event_preprocessor
def only_me_check(bot: Bot):
    # V11Bot & self_id in SUPERUSERS 的消息
    if isinstance(bot, V11Bot) and bot.self_id in SUPERUSERS:
        return

    raise IgnoredException("only superuser!")


try:
    require("nonebot_plugin_alconna")
    from nonebot.plugin import inherit_supported_adapters

    from .patch_alconna import *

    supported_adapters = inherit_supported_adapters("nonebot_plugin_alconna")
except RuntimeError:
    pass

__plugin_meta__ = PluginMetadata(
    name="Ohh My Bot",
    description="我的Bot我做主~",
    usage="无",
    type="library",
    homepage="https://github.com/eya46/nonebot-plugin-omb",
    supported_adapters={"~onebot.v11"},
)
